from unicodedata import name
from rest_framework import routers
from travelblog import views


route = routers.DefaultRouter()
route.register('blog', views.BlogPost)
urlpatterns = route.urls