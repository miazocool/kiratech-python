from functools import reduce
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django_tables2 import tables, SingleTableView, TemplateColumn, Column
import requests

from .forms import InventoryForm
from .models import Inventory
from django.db import models

API_URL = "http://localhost:8000/api/inventory" 
 
# Create your views here.
def index(request):
    return render(request, "crud/index.html")

class InventoryTable(tables.Table):
    view_more = TemplateColumn("<a href=/crud/inventory/detail/{{ record.id }}>Update</a>",
                        verbose_name=('View More'),
                        orderable=False, ) # orderable not sortable
    class Meta:
        model = Inventory
        template_name = "django_tables2/bootstrap.html"
        fields = ["id", "name", 'availability','supplier']
        sequence = ['id', "name", 'availability','supplier']

def details(request, value):
    data = {'name' : 'Hello Inventory'}
    form = InventoryForm(data)
    return render(request, "crud/details.html", {"form": form})

def inventory_list(request):
    try:
        headers = {"Content-Type": "application/json; charset=utf-8; WWW-Authenticate"}
        r = requests.get(API_URL,headers=headers, params=request.GET)
        print (f'Objects retrieved from API : {r.json()}')
        if r.status_code == 200:
            # table = InventoryTable(Inventory.objects.all())
            table = InventoryTable(r.json()["results"])
            return render(request, "crud/listing.html", {
                "table": table
            })
    except requests.exceptions.RequestException as e: 
        raise HttpResponse(f'Could not save data {e}')

# def list_query(request):
#     inv_name = request.GET.get('name')
#     inv = Inventory.objects.filter(name=inv_name)
#     table = InventoryTable(inv)
#     return render(request, "crud/listing.html", {
#         "table": table
#     })