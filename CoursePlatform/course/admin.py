from django.contrib import admin
from .models import Category,SubCategory,Tutorial,TutorialContent,TutorialTag

# Register your models here.


class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name')



class SubCategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','category')


class TutorialAdmin(admin.ModelAdmin):
    list_display=('id','category','subcategory','name','type','no_of_content')



class TutorialContentAdmin(admin.ModelAdmin):
   list_display=('id','tutorial','name','payment_conformation')
  



admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Tutorial,TutorialAdmin)
admin.site.register(TutorialContent,TutorialContentAdmin)
admin.site.register(TutorialTag)


