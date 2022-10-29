from venv import create
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("inventory/", views.inventory_list, name='list'),
    # path("inventory/", views.InventoryListView.as_view(), name='list'),
    path("inventory/<int:id>", views.details, name='details'),
]