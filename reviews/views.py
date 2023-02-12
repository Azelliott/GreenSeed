from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.shortcuts import redirect
from django.urls import reverse
from shop.models import Product
from reviews.models import Review
from checkout.models import OrderItem
from .forms import ReviewForm
from django.contrib import messages



def reviews(request, product_id):
    '''A view to return the reviews page'''
    product = get_object_or_404(Product, id=product_id)
    order_item = OrderItem.objects.filter(product=product, order__user_profile=request.user.userprofile).first()

    if order_item:
        review = Review.objects.filter(order_item=order_item, user_profile=request.user.userprofile).first()
        if review:
            return redirect('product-details', product_id=product_id)
        form = ReviewForm()
        if request.method == 'POST':
            form = ReviewForm(request.POST)
            if form.is_valid():
                review = form.save(commit=False)
                review.user_profile = request.user.userprofile
                review.order_item = order_item
                review.product = product
                review.save()
                messages.success(request, f'Your review for {product.name} was successfully posted!')
                return redirect('product-details', product_id=product_id)
        return render(request, 'reviews/review.html', {'product': product, 'form': form, 'review': review, 'order_item': order_item})
    return redirect('product-details', product_id=product_id)