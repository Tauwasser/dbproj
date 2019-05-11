from django.urls import path

from . import views

urlpatterns = [
    path('',                  views.index, name='index'),
    path('<str:system_slug>', views.index, name='index'),
    path('<str:system_slug>/<str:pcb_slug>', views.details, name='details'),
]
