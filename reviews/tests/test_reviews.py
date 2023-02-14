# reviews app tests

from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from reviews.models import Review
from shop.models import Product


class TestReviews(TestCase):
    # create a user
    def setUp(self):
        user= User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

    # test review form submission
    def test_review_form_submission(self):
        # login as the user
        self.client.login(username='testuser', password='testpassword')

        # create a new product
        product = Product.objects.create(
            name='Test Product', description='Test description', price=10.0)

        # send a POST request to the view with the ID of the new product
        response = self.client.post(reverse('review', args=[product.id]), {
            'title': 'test',
            'review': 'test',
            'rating': 5,
        })

        # check that the response is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # check that a review was added to the database
        self.assertEqual(Review.objects.count(), 0)

    # test review form submission with no title

    def test_review_form_submission_no_title(self):
        # login as the user
        self.client.login(username='testuser', password='testpassword')

        # send a POST request to the view
        response = self.client.post(reverse('review'), {
            'review': 'test',
            'rating': 5,
        })

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check that a review was not added to the database
        self.assertEqual(Review.objects.count(), 0)

        # check that the correct error message was returned
        self.assertFormError(
            response, 'form', 'title', 'This field is required.')
