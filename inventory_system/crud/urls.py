from venv import create
from django.urls import path, re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("inventory/", views.inventory_list, name='list'),
    path("inventory/<int:id>", views.details, name='details'),
    # re_path(r'^inventory/(\d{4})/$', views.details, name="details"),
    # re_path(r'^inventory/(?P<id>[0-9]{1})/$', views.list_query, name='list-query'),
    # re_path(r'^inventory/(?P<id>\w{1,50})/$', views.list_query, name='list-query'),
    # path(r'inventory/?', views.inventory_list, name='list-query'),
    # path("inventory/", views.InventoryListView.as_view(), name='list'),
]