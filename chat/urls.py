# chat/urls.py
# map URLs to views here
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('<str:room_name>/', views.room, name='room'),
]