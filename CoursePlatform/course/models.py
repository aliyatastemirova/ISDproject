from django.db import models
from django.contrib import admin



# Create your models here.


#creates the table name course_category with different fields like name,slug and created.we dont need to mention primary key here coz it is maintained by framework

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

#It helps to return the name of category
    def __str__(self):
                return self.name

   
       

class SubCategory(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
   
    def __str__(self):
                return self.name

   

class Tag(models.Model):
        name=models.CharField(max_length=50)
        slug=models.SlugField(unique=True)
        subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
        created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
                return self.name

       