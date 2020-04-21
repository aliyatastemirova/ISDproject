from django.contrib import admin
from .models import Category,SubCategory,Tag

# Register your models here.




class CategoryAdmin(admin.ModelAdmin):
    list_display=('id','name')



class SubCategoryAdmin(admin.ModelAdmin):
    list_display=('id','name','category')


class TagAdmin(admin.ModelAdmin):
    list_display=('id','name','subcategory')


admin.site.register(Category,CategoryAdmin)
admin.site.register(SubCategory,SubCategoryAdmin)
admin.site.register(Tag,TagAdmin)

