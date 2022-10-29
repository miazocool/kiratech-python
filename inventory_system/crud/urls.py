from venv import create
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("inventory/", views.LinkListView.as_view(), name='list'),
    path("inventory/detail", views.details, name='details'),
]