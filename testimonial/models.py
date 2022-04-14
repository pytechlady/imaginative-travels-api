from django.db import models

# Create your models here.
class Testimony(models.Model):
    name = models.CharField(max_length=200)
    job = models.CharField(max_length=100)
    testimony = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name
