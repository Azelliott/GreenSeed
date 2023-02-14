# unit tests for the shop app

from django.test import TestCase
from django.contrib.auth.models import User
from shop.models import Product, Category
from profiles.models import UserProfile
from django.urls import reverse


# tests for shop views
class TestShopViews(TestCase):
    '''Test shop views'''
    # shop view
    def test_shop_view(self):
        # send a GET request to the view
        response = self.client.get(reverse('shop'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check that the view returns the correct template
        self.assertTemplateUsed(response, 'shop/shop.html')

    # product detail view
    def test_product_detail_view(self):
        # create a product
        product = Product.objects.create(
            name='test product',
            price=1.00,
            description='test description',
            image='test.jpg',
        )

        # send a GET request to the view
        response = self.client.get(reverse('product-details', args=[1]))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check that the view returns the correct product
        self.assertEqual(response.context['product'], product)

        # check that the view returns the correct template
        self.assertTemplateUsed(response, 'shop/product-details.html')
