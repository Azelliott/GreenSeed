from django.contrib import admin
from .models import Review
from django import forms
from django.contrib.auth.models import User
from reviews.models import Review


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'order_item', 'rating', 'review_text', 'created_at')
    list_filter = ('order_item', 'rating', 'created_at')

    def product_name(self, obj):
        return obj.order_item.product.name
    product_name.short_description = 'Product Name'

    def review_text(self, obj):
        return obj.text
    review_text.short_description = 'Review Text'

    def created_at(self, obj):
        return obj.order_item.order.created_at
    created_at.short_description = 'Created At'

    def user_name(self, obj):
        return obj.order_item.order.user_profile.user.username


admin.site.register(Review, ReviewAdmin)
