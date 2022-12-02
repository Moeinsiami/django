from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'index'),
    path('mamad', views.mamad , name = 'mamad'),
    path('javad', views.javad , name = 'javad')
]