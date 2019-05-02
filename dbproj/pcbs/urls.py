from django.urls import path

from . import views

urlpatterns = [
    path('',             views.index, name='index'),
    path('<str:system>', views.index, name='index'),
    path('<str:system>/<str:pcb>', views.details, name='details'),
]
