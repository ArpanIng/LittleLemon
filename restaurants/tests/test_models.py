from django.test import TestCase

from restaurants.models import Menu


class MenuTestCase(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80)
        self.assertEqual(str(item), "IceCream", 80)
