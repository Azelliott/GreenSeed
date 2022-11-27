from django.db import models

# Create your models here.

# Model for the contact form on the contact page
class ContactForm(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    message = models.TextField(max_length=500)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name