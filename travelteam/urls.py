from unicodedata import name
from rest_framework import routers
from travelteam import views


router = routers.DefaultRouter()
router.register('team', views.TeamViewSet)
urlpatterns = router.urls