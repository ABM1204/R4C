from django.urls import path
from endpoint.views import get_all_robots, index

urlpatterns = [
    path('', index, name='index'),
    path('robots/', get_all_robots, name='get_all_robots'),
]
