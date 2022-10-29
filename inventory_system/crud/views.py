from functools import reduce
from django.template import loader
from django.http import HttpResponse
from django.views.generic import ListView
from django.shortcuts import redirect, render, get_object_or_404
from django_tables2 import tables, SingleTableView, TemplateColumn, Column
from .models import Inventory, LinkModel, Supplier
from django.db import models
# Create your views here.
def index(request):
    return render(request, 'crud/index.html')

class LinkModelTable(tables.Table):
    supplier_name = Column(accessor = 'supplier.name')
    inventory_name = Column(accessor = 'inventory.name')
    availability = Column(accessor = 'inventory.availability')
    
    class Meta:
        model = LinkModel
        template_name = "django_tables2/bootstrap.html"
        fields = ["id"]
        sequence = ['id']
    # view_more = TemplateColumn(verbose_name=('Action'),
    #                         template_name='crud/view-more.html',
    #                         orderable=False)  # orderable not sortable

class LinkListView(SingleTableView):
    model = LinkModel
    table_class = LinkModelTable
    template_name = 'crud/listing.html'
