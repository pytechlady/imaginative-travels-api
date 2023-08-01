from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
class Blog(models. Model):
    
    category_choice = (
        ("Lifestyle", "Lifestyle"),
        ("Food", "Food"),
        ("Culture", "Culture"),
        ("Attractions", "Attractions"),
        ("News", "News"),
        ("Generic", "Generic"),
    )
    
    title = models.CharField(max_length=200)
    content = RichTextField()
    category = models.CharField(choices=category_choice, max_length=20)
    travelphoto = models.CharField(max_length=255)
    travelphoto_2 = models.CharField(max_length=255, blank=True, null=True)
    travelphoto_3 = models.CharField(max_length=255, blank=True, null=True)
    travelphoto_4 = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
