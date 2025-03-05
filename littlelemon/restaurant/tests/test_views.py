from django.test import TestCase
from restaurant.models import Menu
from restaurant.serializers import MenuSerializer

class MenuViewTest(TestCase):
    def setUp(self):
        self.item1 = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.item2 = Menu.objects.create(title="Margarita", price=30, inventory=10)
        self.item3 = Menu.objects.create(title="Hamburger", price=120, inventory=50)
    
    def test_getall(self):
        queryset = Menu.objects.all().order_by("id")
        serialized_data = MenuSerializer(queryset, many=True).data
        expected_data = [
            {"id": self.item1.id, "title": "IceCream", "price": "80.00", "inventory": 100},
            {"id": self.item2.id, "title": "Margarita", "price": "30.00", "inventory": 10},
            {"id": self.item3.id, "title": "Hamburger", "price": "120.00", "inventory": 50},
        ]

        # Assert the serialized data matches the expected data
        self.assertEqual(serialized_data, expected_data)
        