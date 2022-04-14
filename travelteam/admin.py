from django.contrib import admin
from .models import Team
from django.utils.html import format_html

# Register your models here.

class TeamAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{0}" width="40" style="border-radius: 50%"/>'.format(object.image.url))
    
    thumbnail.short_description = 'Photo'
    
    list_display = ('id', 'thumbnail', 'title', 'first_name', 'last_name' )
    list_display_links = ('id', 'thumbnail', 'title', 'first_name', 'last_name')
    search_fields = ('id', 'title', 'first_name', 'last_name')
    list_filter = ('title',)
    
admin.site.register(Team, TeamAdmin)