from django.db import models
from datetime import datetime

# Create your models here.
class Supplier(models.Model):
    name = models.CharField(max_length=200, verbose_name="Supplier name",)
    date_created = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return f'Supplier id : %d; name : %s;' % (self.id, self.name)

class Inventory(models.Model):
    name = models.CharField(max_length=200, verbose_name="Inventory name",)
    description = models.CharField(max_length=500)
    note = models.TextField()
    stock = models.IntegerField()
    availability = models.BooleanField()
    date_created = models.DateTimeField(default=datetime.now())
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    def __str__(self):
        return f'Inventory id : %d; name : %s; availability : %s;' % (self.id, self.name , self.availability)
# Create your models here.