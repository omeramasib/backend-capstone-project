from django.test import TestCase
from restaurant.models import Menu

class MenuViewTest(TestCase):
    def setUp(self):
        self.Menu = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)


    def test_get_item(self):
        self.assertIsInstance(self.Menu.Title, str)