from django.db import models


# Model for the contact form on the contact page
class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


# Model for the newsletter form on the home page
class NewsletterForm(models.Model):
    email = models.EmailField()
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
