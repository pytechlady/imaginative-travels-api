from rest_framework import viewsets
from travelteam.models import Team
from travelteam.serializers import TeamSerializer
from .pagination import CustomPagination

# Create your views here.

class TeamViewSet(viewsets.ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    pagination_class = CustomPagination