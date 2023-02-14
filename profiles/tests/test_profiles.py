from django.test import TestCase
from django.contrib.auth.models import User
from profiles.models import UserProfile
from django.urls import reverse
from checkout.models import Order


class TestProfiles(TestCase):
    def test_profile_view(self):
        # create a user
        user = User.objects.create_user(
            username='testuser',
            password='testpassword'
        )

        # login as the user
        self.client.login(username='testuser', password='testpassword')

        # send a GET request to the view
        response = self.client.get(reverse('my_account'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check that the view returns the correct user
        self.assertEqual(response.context['user'], user)


