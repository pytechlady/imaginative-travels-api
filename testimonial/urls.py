from unicodedata import name
from rest_framework import routers
from testimonial import views


testimonials = routers.DefaultRouter()
testimonials.register('testimonial', views.TestimonialViewSet)
urlpatterns = testimonials.urls