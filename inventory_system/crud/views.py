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
    return render(request, 'crud/index.html')

class InventoryTable(tables.Table):
    # supplier = Column(accessor = 'supplier.name')
    # availability = Column(accessor = 'availability')
    # clickable = {'td': {'data-href': lambda record: record.id}}
    # attrs=clickable
    # view_more = TemplateColumn(verbose_name=('View More'),
    #                         template_name='crud/view-more.html',
    #                         orderable=False, ) # orderable not sortable
    view_more = TemplateColumn("<a href=/crud/inventory/detail/{{ record.id }}>Update</a>",
                        verbose_name=('View More'),
                        orderable=False, ) # orderable not sortable
    foo = TemplateColumn("{{ record.url }}")
    print(f'the id is {foo.value}')
    class Meta:
        model = Inventory
        template_name = "django_tables2/bootstrap.html"
        fields = ["id", "name", 'availability','supplier']
        sequence = ['id', "name", 'availability','supplier']
        exclude = ("foo",)
        # row_attrs = {
        #     "onClick": lambda record: "document.location.href='/crud/inventory/detail/{0}';".format(record.name)
        #     # "onClick": lambda record: print(f"the record is : {record}")
        # }

# class InventoryListView(SingleTableView):
#     model = Inventory
#     data = [
#         {"name" :"Inv5", "supplier" : "12"},
#         {"name" : "Inv6", "supplier" : "12"},
#         {"name" : "Inv7", "supplier" : "13"}
#     ]
#     table_class = InventoryTable
#     table = InventoryTable(data)
#     template_name = 'crud/listing.html'

def details(request, value):
    # form = InventoryForm()
    data = {'name' : 'Hello Inventory'}
    form = InventoryForm(data)
    print("value is:" + value)
    # if request.method == "GET":
    #     print(request)
    #     user = Inventory(name=request.POST.get('name'),
    #                 favorite_quote=request.POST.get('favorite_quote'))
    #     user.save()
    #     return render(request, "crud/listing.html")
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