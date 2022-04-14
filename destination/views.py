from rest_framework import viewsets
from destination.models import Destination
from destination.serializers import DestinationSerializer
from .pagination import CustomPagination

# Create your views here.

class DestinationViewSet(viewsets.ModelViewSet):
    queryset = Destination.objects.all()
    serializer_class = DestinationSerializer
    pagination_class = CustomPagination