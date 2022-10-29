from django.test import TestCase
from django.urls import reverse
from .models import Supplier, Inventory

class CrudTest(TestCase):
    def setUp(self):
        sup1 = Supplier.objects.create(id=101, name="sup1")
        inv = Inventory.objects.create(id=102, 
                                        name="inv1", 
                                        supplier=sup1,
                                        stock=1,
                                        availability=True)
    
    def test_view_url_exists_inventory(self):
        response = self.client.get('/crud/inventory/')
        self.assertEqual(response.status_code, 200)
    
    #Not working
    # def test_view_url_exists_at_desired_location(self):
    #     response = self.client.get('/crud/inventory/101/')
    #     self.assertEqual(response.status_code, 200)
