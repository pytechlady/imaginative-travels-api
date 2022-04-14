from unicodedata import name
from rest_framework import routers
from destination import views


routes = routers.DefaultRouter()
routes.register('destinations', views.DestinationViewSet)
urlpatterns = routes.urls