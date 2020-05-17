from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Category,SubCategory,Course,CourseContent,CourseTag
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.



#It is the defination of the subcategory field shown in category forms
class SubCategoryInline(admin.TabularInline):
    fields=['name','slug']
    model = SubCategory
    extra = 2



class CategoryAdmin(admin.ModelAdmin):
    #It will display the id,name and created in list view of this specific model
    list_display=('id','name','created')

    #It will create the link on that specified columns
    list_display_links=('id','name','created')

    #It will show the fields listed on 'fields' column on the backend form
    fieldsets = [
        ('Category',               {'fields': ['name','slug']}),
    
    ]

    #It will show subcateogry option in Category creation and edit form
    inlines = [SubCategoryInline]

    


class SubCategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','category','created')
    list_display_links=('id','name','category','created')





class TagInline(admin.TabularInline):
    fields=['name','slug']
    model = CourseTag
    extra = 2

class ContentInline(admin.StackedInline):
    fields=['course','name','video_url','objective','description','payment_confirmation','sort_order']
    model = CourseContent
    extra = 1


class CourseAdmin(SummernoteModelAdmin):

    list_display=('id','category','subcategory','name','no_of_content','image_display')
    list_display_links=('id','category','subcategory','name')
    fieldsets = [
        ('Basic Details',{'fields': ['category','subcategory','name','no_of_content','slug','price','thumbnail']}),
        ('Information', {'fields': ['what_student_will_learn','description','prerequisite','who_this_course_is_for'], 'classes': ['collapse']}),
    ]
    summernote_fields=('description','what_student_will_learn','prerequisite','who_this_course_is_for')
   
    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
                return qs
        return qs.filter(created_by=request.user)
        
   
    def save_model(self, request, obj, form, change):
          obj.created_by =request.user
          super().save_model(request, obj, form, change)

    inlines = [TagInline,ContentInline]
   




class CourseContentAdmin(AdminVideoMixin,admin.ModelAdmin):
   list_display=('id','course','name')
   list_display_links=('id','name')
   fields=['course','name','video_url','objective','description','payment_confirmation','sort_order']

   def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
                return qs
        return qs.filter(created_by=request.user)

   
   



admin.site.register(Category,CategoryAdmin)
# admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Course,CourseAdmin)
admin.site.register(CourseContent,CourseContentAdmin)



