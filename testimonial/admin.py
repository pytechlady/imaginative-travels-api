from django.contrib import admin
from .models import Testimony

# Register your models here.

class TestimonialAdmin(admin.ModelAdmin):
    
    list_display = ('id', 'name', 'job')
    list_display_links = ('id', 'name', 'job')
    search_fields = ('id', 'name', 'job')
    list_filter = ('name', 'job')
    
admin.site.register(Testimony, TestimonialAdmin)