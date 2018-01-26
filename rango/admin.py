from django.contrib import admin
from rango.models import Category, Page


# Add in this class to customise the Admin Interface
class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')


# Register your models here.
admin.site.register(Category)
admin.site.register(Page, PageAdmin)