# unit tests for the shop app

from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import Product, Category
from profiles.models import UserProfile
from django.urls import reverse


# tests for shop views
class TestShopViews(TestCase):
    '''Test shop views'''
    def test_all_products_view(self):
        # send a GET request to the view
        response = self.client.get(reverse('all-products'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/all-products.html')
