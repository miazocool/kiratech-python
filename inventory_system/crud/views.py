from functools import reduce
from django.template import loader
from django.http import HttpResponse
from django.urls import reverse
from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django_tables2 import tables, SingleTableView, TemplateColumn, Column
import requests

from .forms import InventoryForm
from .models import Inventory, Supplier
from django.db import models

API_URL = "http://localhost:8000/api/inventory" 
 
# Create your views here.
def index(request):
    return render(request, "crud/index.html")

class InventoryTable(tables.Table):
    supplier = Column(accessor = 'supplier.name')
    view_more = TemplateColumn("<a href=/crud/inventory/{{ record.id }}>Details</a>",
                        verbose_name=('Action'),
                        orderable=False, ) # orderable not sortable
    class Meta:
        model = Inventory
        template_name = "django_tables2/bootstrap.html"
        fields = ["id", "name", 'availability','supplier']
        sequence = ['id', "name", 'availability','supplier']

def details(request, id):
    inv_object = Inventory.objects.filter(id=id)
    # print(f'inv_object is : inv_object[0]['name']')
    data = {'name' : inv_object[0].name,
            'description' : inv_object[0].description,
            'note' : inv_object[0].note,
            'stock' : inv_object[0].stock,
            'availability' : inv_object[0].availability
            }
    form = InventoryForm(data)
    return render(request, "crud/details.html", {"form": form})

def inventory_list(request):
    querying_name = request.GET.get('name', None)
    if querying_name:
        print("query id is " + querying_name)
        inv = Inventory.objects.filter(name=querying_name)
        table = InventoryTable(inv)
        return render(request, "crud/listing.html", {
            "table": table
        })
    try:
        inv_object = Inventory.objects.all()
        if inv_object :
            table = InventoryTable(inv_object)
            return render(request, "crud/listing.html", {
                "table": table
            })

        # Get api to fetch inventory data
        # Populating crud inventory table from external API
        headers = {"Content-Type": "application/json; charset=utf-8; WWW-Authenticate"}
        r = requests.get(API_URL,headers=headers, params=request.GET)
        print (f'Objects retrieved from API : {r.json()}')
        inv_array = r.json()["results"]
        for inv_el in inv_array :
            sup = Supplier.objects.create(
                name=inv_el["supplier"][1]
            )
            Inventory.objects.create(
                name=inv_el["name"], 
                description=inv_el["description"], 
                note=inv_el["note"], 
                stock=inv_el["stock"], 
                availability=inv_el["availability"], 
                supplier=sup
                )
        table = InventoryTable(inv_object)
        return render(request, "crud/listing.html", {
            "table": table
        })
    except requests.exceptions.RequestException as e: 
        raise HttpResponse(f'Could not save data {e}')

# def list_query(request):
#     print("Hello World")
#     inv_name = request.GET.get('name')
#     print(inv_name)
#     inv = Inventory.objects.filter(name=inv_name)
#     table = InventoryTable(inv)
#     return render(request, "crud/listing.html", {
#         "table": table
#     })