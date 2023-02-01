from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer


class MenuViewTest(TestCase):
    def setUp(self):
        self.food = Menu.objects.create(title='Food', price=150, inventory=12)
        self.appetizer = Menu.objects.create(title='Appetizer', price=60, inventory=500)

    def test_getall(self):
        all_menu = Menu.objects.all()
        serialized_menu = MenuSerializer(instance=all_menu, many=True).data
        json_menu = [dict(sm) for sm in serialized_menu]
        expected_values = [{'id': 1, 'title': 'Food', 'price': '150.00', 'inventory': 12},
                           {'id': 2, 'title': 'Appetizer', 'price': '60.00', 'inventory': 500}]
        self.assertEqual(json_menu, expected_values)
