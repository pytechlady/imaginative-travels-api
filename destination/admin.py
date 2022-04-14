from django.contrib import admin
from .models import Destination
from django.utils.html import format_html

# Register your models here.

class DestinationAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{0}" width="40" style="border-radius: 50%"/>'.format(object.destination_image.url))
    
    thumbnail.short_description = 'Photo'
    
    list_display = ('id', 'thumbnail', 'destination_title')
    list_display_links = ('id', 'thumbnail', 'destination_title')
    search_fields = ('destination_title',)
    list_filter = ('destination_title',)
    
admin.site.register(Destination, DestinationAdmin)