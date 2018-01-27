from django.contrib import admin
from rango.models import Category, Page


# Add in this class to customise the Admin Interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


# Add in this class to customise the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

# Register your models here.
# Update the registration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page, PageAdmin)