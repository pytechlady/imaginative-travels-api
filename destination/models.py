from django.db import models

# Create your models here.
class Destination(models.Model):
    destination_title = models.CharField(max_length=20)
    description = models.TextField()
    destination_image = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.destination_title