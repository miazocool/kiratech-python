from functools import reduce
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django_tables2 import tables, SingleTableView, TemplateColumn, Column

from .forms import InventoryForm
from .models import Inventory, LinkModel, Supplier
from django.db import models
# Create your views here.
def index(request):
    return render(request, 'crud/index.html')

class LinkModelTable(tables.Table):
    supplier_name = Column(accessor = 'supplier.name')
    inventory_name = Column(accessor = 'inventory.name')
    availability = Column(accessor = 'inventory.availability')
    view_more = TemplateColumn(verbose_name=('View More'),
                            template_name='crud/view-more.html',
                            orderable=False)  # orderable not sortable
    class Meta:
        model = LinkModel
        template_name = "django_tables2/bootstrap.html"
        fields = ["id"]
        sequence = ['id']

class LinkListView(SingleTableView):
    model = LinkModel
    table_class = LinkModelTable
    template_name = 'crud/listing.html'

def details(request):
    # form = InventoryForm()
    data = {'name' : 'Hello Inventory'}
    form = InventoryForm(data)
    # if request.method == "GET":
    #     print(request)
    #     user = Inventory(name=request.POST.get('name'),
    #                 favorite_quote=request.POST.get('favorite_quote'))
    #     user.save()
    #     return render(request, "crud/listing.html")
    return render(request, "crud/details.html", {"form": form})
