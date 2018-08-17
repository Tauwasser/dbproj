from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('ajax/find_games/', views.find_games, name='find_games'),
]
