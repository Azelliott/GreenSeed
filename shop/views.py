from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from .models import Product, Category


# Online shop page
def shop(request):
    '''A view to return the shop page'''
    return render(request, 'shop/shop.html')


# Online shop products page
def shop_products(request, category_slug=None):
    '''A view to return the shop products page'''
    products = Product.objects.all()

    # If a category slug is provided, filter the products based on the category
    if category_slug:
        if category_slug == 'plants':
            categories = ['bonsai', 'cacti', 'succulents', 'house_plants',
                          'garden_plants', 'carnivorous_plants']
            products = products.filter(category__slug__in=categories)
        elif category_slug == 'accessories':
            categories = ['pots_and_planters', 'fertilizers_and_pesticides']
            products = products.filter(category__slug__in=categories)
        elif category_slug != 'all-products':
            category = get_object_or_404(Category, slug=category_slug)
            products = products.filter(category=category)

    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
    }
    return render(request, 'shop/shop-products.html', context)
