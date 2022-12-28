from django.db import models


# Category model
class Category(models.Model):
    '''Category model'''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return f"{self.name} ({self.slug})"

    def get_friendly_name(self):
        return self.friendly_name

    def __str__(self):
        return self.description
