from django.test import TestCase

# Create your tests here.
class ApiTest(TestCase):
    def test_get_inventory(self):
        response = self.client.get('/api/inventory/')
        self.assertEqual(response.status_code, 200)