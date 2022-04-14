from django.contrib import admin
from .models import Contact

# Register your models here.

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone_number')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('id', 'first_name', 'last_name')
    list_filter = ('first_name', 'last_name')
    
admin.site.register(Contact, ContactAdmin)