from django.contrib import admin
from embed_video.admin import AdminVideoMixin
from .models import Category,SubCategory,Tutorial,TutorialContent,TutorialTag

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
    model = TutorialTag
    extra = 2


class TutorialAdmin(admin.ModelAdmin):
    list_display=('id','category','subcategory','name','no_of_content')
    list_display_links=('id','category','subcategory','name')
    fieldsets = [
        ('Basic Details',{'fields': ['category','subcategory','name','no_of_content','slug']}),
        ('Information', {'fields': ['what_student_will_learn','description','prerequisite','who_this_course_is_for'], 'classes': ['collapse']}),
    ]
    inlines = [TagInline]



class TutorialContentAdmin(AdminVideoMixin,admin.ModelAdmin):
   list_display=('id','tutorial','name','payment_conformation')
   list_display_links=('id','tutorial','name')
   fields=['tutorial','name','video_url','objective','description','payment_conformation','sort_order']
   



admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(TutorialContent,TutorialContentAdmin)



