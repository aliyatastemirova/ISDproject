from django.db import models
from django.contrib import admin
from django.utils.html import escape



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

   


class Tutorial(models.Model):
        name=models.CharField(max_length=255)
        slug=models.SlugField(unique=True)
        what_student_will_learn=models.TextField()
        description=models.TextField()
        prerequisite=models.TextField()
        who_this_course_is_for=models.TextField()
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)

        type_of_tutorial = [
        ('video/audio', 'Video/Audio'),
        ('pdf', 'pdf'),
        ('ebook', 'ebook'),
         ]
        type=models.CharField(max_length=100,choices=type_of_tutorial)
        no_of_content=models.PositiveIntegerField()
        created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
                     return self.name




class TutorialTag(models.Model):
        tutorial=models.ForeignKey(Tutorial,on_delete=models.CASCADE)
        name=models.CharField(max_length=50)
        slug=models.SlugField(unique=True)
        created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
                     return self.name


class TutorialContent(models.Model):
      tutorial=models.ForeignKey(Tutorial,on_delete=models.CASCADE)
      name=models.CharField(max_length=255)
      video_url=models.CharField(max_length=255,default=None)
      file1=models.ImageField(default='',upload_to='course/uploads/%Y/%m/%d/ ')
      file2=models.ImageField(default='',upload_to='course/uploads/%Y/%m/%d/')
      file3=models.ImageField(default='',upload_to='course/uploads/%Y/%m/%d/')
      sort_order=models.PositiveSmallIntegerField()
      objective=models.TextField()
      description=models.TextField()
      value = [
        (1, 'Yes'),
        (0, 'No'),
         ]
      payment_conformation=models.PositiveSmallIntegerField(choices=value)

      def __str__(self):
                     return self.name

      




