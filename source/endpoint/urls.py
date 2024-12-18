from django.urls import path
from endpoint.views import get_all_robots

urlpatterns = [
    path('robots/', get_all_robots, name='get_all_robots'),
]
