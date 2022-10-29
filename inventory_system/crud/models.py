from statistics import mode
from typing import Text
from unittest.util import _MAX_LENGTH
from django.db import models
from datetime import datetime

# Create your models here.
class Inventory(models.Model):
    name = models.CharField(max_length=200)
    description = models.CharField(500)
    note = models.Text()
    stock = models.IntegerField()
    availability = models.BooleanField()
    #Foreign key supplier table
    supplier = models.CharField()
    date_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'Inventory id : %d; name : %s; availability : %s;' % (self.id, self.name , self.availability)

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200)
    date_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'Supplier id : %d; name : %s;' % (self.id, self.name)