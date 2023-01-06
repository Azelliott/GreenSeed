from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import ProductForm
from shop.models import Product, Category


def add_product(request):
    """ Add a product to the store """

    form = ProductForm()

    template = 'management/add_product.html'
    context = {
        'form': form,
    }

    return render(request, template, context)
