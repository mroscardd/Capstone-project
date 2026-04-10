from django.test import TestCase
from restaurant.views import Menu
from restaurant.serializers import MenuSerializer
from rest_framework import status


class MenuViewTest(TestCase):
    def setUp(self):
        Menu.objects.create(title="Carbonara", price=15, inventory=50)
        Menu.objects.create(title="Trufa", price=20, inventory=10)

    def test_getall(self):
        url = '/restaurant/menu/'
        response = self.client.get(url)

        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

        





