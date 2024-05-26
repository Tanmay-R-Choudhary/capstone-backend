from django.test import TestCase
from restaurant.models import *


class MenuViewTest(TestCase):
    def setup(self):
        item1 = Menu.objects.create(
            title="Ice Cream",
            price=80,
            inventory=100
        )
        item2 = Menu.objects.create(
            title="Cake",
            price=80,
            inventory=100
        )
        item3 = Menu.objects.create(
            title="Pie",
            price=80,
            inventory=100
        )
        
        item1.save()
        item2.save()
        item3.save()
        
    def test_getall(self):
        items = Menu.objects.all().values()
        
        res = ['Ice Cream : 80', 'Cake : 80', 'Pie : 80']
        
        for idx, item in enumerate(items):
            self.assertEqual(str(item), res[idx])
        
        