from django.db import models
from django.core.validators import FileExtensionValidator, MinLengthValidator
from decimal import Decimal


# Category model
class Category(models.Model):
    '''Category model'''
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)
    description = models.TextField(max_length=500, null=True, blank=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.description

    def __str__(self):
        return self.slug

    def __str__(self):
        return self.name

    def __str__(self):
        return self.friendly_name

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# Product model
class Product(models.Model):
    '''Product model'''
    category = models.ForeignKey('Category', null=True, blank=True,
                                 on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField(max_length=500, null=True, blank=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(null=True, blank=True)
    availability = models.BooleanField(default=True)
    rating = models.DecimalField(max_digits=2, decimal_places=1, null=True,
                                 blank=True)

    def update_median_rating(self):
        ratings = [r.rating for r in self.review_set.all()]
        ratings.sort()
        if len(ratings) % 2 == 0:
            mid = len(ratings) // 2
            median_rating = (ratings[mid - 1] + ratings[mid]) / 2
        else:
            median_rating = ratings[len(ratings) // 2]
        self.rating = median_rating
        self.save()

    def get_category_name(self):
        '''Returns the name of the category'''
        return self.category.name

    def get_friendly_name(self):
        return self.friendly_name

    def __str__(self):
        return self.description

    def __str__(self):
        return str(self.price)

    def __str__(self):
        return self.availability

    def __str__(self):
        return str(self.rating)

    def __str__(self):
        return self.name
