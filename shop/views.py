from django.shortcuts import render
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from .models import Product, Category


# Online shop page
def shop(request):
    '''A view to return the shop page'''
    return render(request, 'shop/shop.html')


# Online shop products page
def shop_products(request, category_slug=None, search_query=None):
    '''A view to return the shop products page'''
    products = Product.objects.all()

    search_query = request.POST.get('search_query')

        # Filter the products based on the search query
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

    if category_slug == 'plants':
        # Create a Q object for each category in the list
        plants_categories = ['bonsai', 'cacti', 'succulents', 'house_plants', 'garden_plants', 'carnivorous_plants']
        q_objects = [Q(category__slug=category) for category in plants_categories]
        # Combine the Q objects using an OR operator
        combined_q = Q()
        for q in q_objects:
            combined_q |= q
        # Filter the products based on the combined Q object
        products = products.filter(combined_q)
    elif category_slug == 'accessories':
        # Create a Q object for each category in the list
        accessories_categories = ['pots-and-planters', 'fertilizers-and-pesticides']
        q_objects = [Q(category__slug=category) for category in accessories_categories]
        # Combine the Q objects using an OR operator
        combined_q = Q()
        for q in q_objects:
            combined_q |= q
        # Filter the products based on the combined Q object
        products = products.filter(combined_q)
    elif category_slug == 'all-products':
        # No need to filter the products, as we want to show all products
        pass
    elif category_slug:
        # Filter the products based on the category slug
        category_q = Q(category__slug=category_slug)
        products = products.filter(category_q)

    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
    }
    return render(request, 'shop/shop-products.html', context)


# Product detail page
def product_details(request, product_id):
    '''A view to return the product detail page'''
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product,
    }
    return render(request, 'shop/product-details.html', context)