from unicodedata import category
from django.db import models

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
    content = models.TextField()
    category = models.CharField(choices=category_choice, max_length=20)
    travelphoto = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
