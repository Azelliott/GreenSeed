from django.urls import reverse
from django.test import TestCase
from django.utils import timezone
from home.models import NewsletterForm, ContactForm


class HomeViewTests(TestCase):
    def test_index_view(self):
        # send a GET request to the view
        response = self.client.get(reverse('index'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_newsletter_form_submission(self):
        # test post request to newsletter form
        response = self.client.post(reverse('index'), {
            'email': 'test@test.com',
        })

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check that a email was added to the newsletter
        self.assertEqual(NewsletterForm.objects.count(), 1)

    def test_plants_view(self):
        # send a GET request to the view
        response = self.client.get(reverse('plants'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_about_view(self):
        # send a GET request to the view
        response = self.client.get(reverse('about'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

        # check that the view calculates the number of years correctly
        current_year = timezone.now().year
        self.assertEqual(response.context['years'], current_year - 2012)

    def test_contact_view(self):
        # send a GET request to the view
        response = self.client.get(reverse('contact'))

        # check that the response is 200 (OK)
        self.assertEqual(response.status_code, 200)

    def test_contact_form_submission(self):
        # send a POST request to the view with valid form data
        response = self.client.post(reverse('contact'), {
            'name': 'test',
            'email': 'test@test.com',
            'message': 'test',
        })

        # check that a new contact form was created
        self.assertEqual(ContactForm.objects.count(), 1)
