from .models import Blog
from rest_framework import viewsets
from .serializers import BlogSerializer
from .pagination import CustomPagination

# Create your views here.
class BlogPost(viewsets.ModelViewSet):
    serializer_class = BlogSerializer
    queryset = Blog.objects.all().order_by('-created_at')
    pagination_class = CustomPagination
    
    

        