from .models import Testimony
from rest_framework import viewsets
from .serializers import TestimonySerializer
from .pagination import CustomPagination


class TestimonialViewSet(viewsets.ModelViewSet):
    serializer_class = TestimonySerializer
    queryset = Testimony.objects.all()
    pagination_class = CustomPagination