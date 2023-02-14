# tests for checkout
from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from checkout.models import Order
from shop.models import Product, Category


class TestCheckout(TestCase):
    def test_cart_view(self):
        # send a GET request to the view
        response = self.client.get(reverse('view_cart'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check that the view returns the correct template
        self.assertTemplateUsed(response, 'shop/cart.html')

