from django.contrib import admin
from .models import Blog
from django.utils.html import format_html

# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{0}" width="40" style="border-radius: 50%"/>'.format(object.travelphoto))
    
    thumbnail.short_description = 'Photo'
    
    list_display = ('id', 'thumbnail', 'title', 'category')
    list_display_links = ('id', 'thumbnail', 'title')
    search_fields = ('id', 'title', 'category')
    list_filter = ('category',)
    
admin.site.register(Blog, BlogAdmin)

