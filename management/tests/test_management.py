from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from checkout.models import Order
from shop.models import Product, Category


class TestManagement(TestCase):
    # test management views
    def test_management_view(self):
        # log in as regular user
        self.client.login(username='testuser', password='testpassword')

        # send a GET request to the view
        response = self.client.get(reverse('add_product'))

        # check that the response is 302 (Forbidden)
        self.assertEqual(response.status_code, 302)

    @classmethod
    def setUpTestData(cls):
        cls.admin = User.objects.create_superuser(
            username='admin',
            email='admin@example.com',
            password='test_password'
        )

    # test admin login
    def test_admin_login(self):
        self.client.login(
            username=self.admin.username, password='test_password')

        # send a GET request to the view
        response = self.client.get(reverse('add_product'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

    # test add product view
    def test_add_product_view(self):
        self.client.login(
            username=self.admin.username, password='test_password')

        # send a GET request to the view
        response = self.client.post(reverse('add_product'), {
            'name': 'test',
            'description': 'test',
            'price': 10,
            'image': 'test.jpg',
            'category': 'test',
            'stock': 10,
        })

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check that a new product was created
        self.assertEqual(Product.objects.count(), 0)



