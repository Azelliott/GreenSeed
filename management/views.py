from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from shop.models import Product, Category
from shop.views import product_details


@login_required
def add_product(request):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product-details', args=[product.id]))
        else:
            messages.error(request, 'Failed to add product. Please ensure the form is valid.')

    form = ProductForm()

    template = 'management/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
