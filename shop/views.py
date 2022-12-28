from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Product


# Online shop page
def shop(request):
    '''A view to return the shop page'''
    return render(request, 'shop/shop.html')


def shop_products(request):
    '''A view to return the shop products page'''
    products = Product.objects.all()
    paginator = Paginator(products, 12) # Show 25 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
    }
    return render(request, 'shop/shop-products.html', context)