from django.db import models
from checkout.models import OrderItem
from profiles.models import UserProfile
from shop.models import Product


class Review(models.Model):
    '''Customer review model'''

    user_profile = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name='reviews')
    product = models.ForeignKey(
        Product, related_name='review_set', on_delete=models.CASCADE)

    order_item = models.ForeignKey(OrderItem, null=False, blank=False,
                                   on_delete=models.CASCADE,
                                   related_name='reviews')
    rating = models.DecimalField(max_digits=3, decimal_places=1,
                                 null=False, blank=False)
    text = models.TextField(null=False, blank=False)

    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('order_item', 'text')

    def save(self, *args, **kwargs):
        '''Check if the order item was already reviewed'''
        if self.order_item.reviews.filter(text=self.text).exists():
            raise Exception("This product has already been reviewed!")
        super().save(*args, **kwargs)
        self.order_item.product.update_median_rating()

    @property
    def median_rating(self):
        '''Return median rating for the product'''
        reviews = self.order_item.product.reviews.all()
        ratings = [r.rating for r in reviews]
        ratings.sort()
        if len(ratings) % 2 == 0:
            mid = len(ratings) // 2
            return (ratings[mid - 1] + ratings[mid]) / 2
        else:
            return ratings[len(ratings) // 2]

    def __str__(self):
        return f'Review for product: {self.order_item.product.name} by user {self.order_item.order.user_profile.user.username}'

