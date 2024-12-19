from django.urls import path
from endpoint.views import get_all_robots, index, generate_robot_summary

urlpatterns = [
    path('', index, name='index'),
    path('robots/', get_all_robots, name='get_all_robots'),
    path('robots-docs/', generate_robot_summary, name='download_robot_summary'),
]
