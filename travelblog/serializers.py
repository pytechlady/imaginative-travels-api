from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Blog
        fields = [
            'id','title', 'content', 'category', 'travelphoto', 'travelphoto_2', 'travelphoto_3', 'travelphoto_4', 'created_at']
        read_only_fields = ['id', 'created_at']
        
