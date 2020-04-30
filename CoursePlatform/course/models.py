from django.db import models
from django.contrib import admin
from django.utils.html import escape
from embed_video.fields import EmbedVideoField
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User



# Create your models here.


#creates the table name course_category with different fields like name,slug and created.we dont need to mention primary key here coz it is maintained by framework

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)

#It helps to return the name of category
    def __str__(self):
                return self.name

    class Meta:
        verbose_name_plural = "Category"

   
       

class SubCategory(models.Model):
    name=models.CharField(max_length=50)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    slug=models.SlugField(unique=True)
    created = models.DateTimeField(auto_now_add=True, null=True)
   
    def __str__(self):
                return self.name
    class Meta:
        verbose_name_plural = "SubCategory"

   


class Course(models.Model):
        name=models.CharField(max_length=255)
        slug=models.SlugField(unique=True)
        what_student_will_learn=models.TextField(null= True,help_text="What Student will learn",blank=True)
        description=models.TextField()
        prerequisite=models.TextField(null= True,help_text="What Student Should Learn Before Enrolling to this Course",blank=True)
        who_this_course_is_for=models.TextField(null= True,help_text="Who this course can target",blank=True)
        category=models.ForeignKey(Category,on_delete=models.CASCADE)
        subcategory=models.ForeignKey(SubCategory,on_delete=models.CASCADE)
        no_of_content=models.PositiveIntegerField()
        created = models.DateTimeField(auto_now_add=True, null=True)
        # created_by=models.ForeignKey(User)
        value = [
        (1, 'Active'),
        (0, 'Inactive'),
         ]
        status=models.PositiveSmallIntegerField(choices=value,default=1)
        price=models.DecimalField(help_text="Price of course on Dollars",max_digits=6, decimal_places=2)
        thumbnail=models.ImageField(upload_to='course')
 
        def __str__(self):  
                     return self.name

        def image_display(self):
                  
                      from django.utils.html import escape
                      return u'<img src="%s" />' % escape(self.thumbnail.url)
                  
        image_display.short_description = 'Image'
        image_display.allow_tags = True

        class Meta:
            verbose_name_plural = "Course"

        # def save_model(self, request, obj, form, change):
        #   obj.user = request.user
        #   super(Post, self).save_model(request, obj, form, change)




class CourseTag(models.Model):
        course=models.ForeignKey(Course,on_delete=models.CASCADE)
        name=models.CharField(max_length=50)
        slug=models.SlugField(unique=True)
        created = models.DateTimeField(auto_now_add=True, null=True)

        def __str__(self):
                     return self.name


class CourseContent(models.Model):
      course=models.ForeignKey(Course,on_delete=models.CASCADE)
      name=models.CharField(max_length=255,help_text="Name of the Eposide")
      video_url=EmbedVideoField(help_text="Enter the Video url of youtube or vimeo")
      sort_order=models.PositiveSmallIntegerField(default=1)
      objective=models.TextField(blank=True,null=True)
      description=models.TextField(help_text="Detail about this Eposide")
      value = [
        (1, 'Yes'),
        (0, 'No'),
         ]
      payment_confirmation=models.PositiveSmallIntegerField(choices=value,default=1)

      def __str__(self):
                     return self.name

      def video(self):
                    return mark_safe('<iframe src="%s" />' % (self.video_url))
      video.short_description = 'Thumbnail'
      video.allow_tags = True

      class Meta:
        verbose_name_plural = "Course Insight"

      




