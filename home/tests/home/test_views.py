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

        # fill out the form and submit it
        response = self.client.post(reverse('contact'), {
            'name': 'test',
            'email': 'test@test.com',
            'message': 'test',
        })

        # check that the response is 302 (redirect)
        self.assertEqual(response.status_code, 302)

        # check that a new contact form was created
        self.assertEqual(ContactForm.objects.count(), 1)

        # check that the contact form was created with the correct data
        contact_form = ContactForm.objects.first()
        self.assertEqual(contact_form.name, 'test')
        self.assertEqual(contact_form.email, 'test@test.com')
        self.assertEqual(contact_form.message, 'test')

        # check that the contact form was created with the correct date
        self.assertEqual(contact_form.date.year, timezone.now().year)
        self.assertEqual(contact_form.date.month, timezone.now().month)
        self.assertEqual(contact_form.date.day, timezone.now().day)

