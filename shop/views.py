from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.shortcuts import get_object_or_404
from django.db.models import Q
from django.http import JsonResponse
from decimal import Decimal
from django.conf import settings
from django.contrib import messages
from .models import Product, Category


# Online shop page
def shop(request):
    '''A view to return the shop page'''
    return render(request, 'shop/shop.html')


# Online shop products page
def shop_products(request, category_slug=None, search_query=None):
    '''A view to return the shop products page'''
    products = Product.objects.all()
    search_query = request.GET.get('search_query')

    # Filter the products based on the search query
    if search_query:
        products = products.filter(
            Q(name__icontains=search_query) | 
            Q(description__icontains=search_query)
        )

    if category_slug == 'plants':
        # Create a Q object for each category in the list
        plants_categories = ['bonsai', 'cacti', 'succulents', 'house_plants',
                             'garden_plants', 'carnivorous_plants']
        q_objects = [Q(category__slug=category) for category in plants_categories]
        # Combine the Q objects using an OR operator
        combined_q = Q()
        for q in q_objects:
            combined_q |= q
        # Filter the products based on the combined Q object
        products = products.filter(combined_q)
    elif category_slug == 'accessories':
        # Create a Q object for each category in the list
        accessories_categories = ['pots-and-planters',
                                  'fertilizers-and-pesticides']
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

    # Get the category object
    category, created = Category.objects.get_or_create(slug=category_slug)
    category_name = category.friendly_name

    if category_slug == 'plants':
        category_name = 'Plants'
    elif category_slug == 'accessories':
        category_name = 'Accessories'
    elif category_slug == 'all-products':
        category_name = 'All Products'
    else:
        category_name = category.friendly_name

    paginator = Paginator(products, 12)  # Show 12 products per page
    page = request.GET.get('page')
    products = paginator.get_page(page)
    context = {
        'products': products,
        'category_name': category_name,
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


# View cart page
def view_cart(request):
    '''A view to return the view cart page'''
    cart = request.session.get('cart', {})
    return render(request, 'shop/cart.html', {'cart': cart})


# Add item to cart
def add_item(request, product_id):
    '''Add a quantity of the specified product to the cart'''
    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart
    messages.success(request, f'Added {quantity} item(s) to your cart')

    return redirect(redirect_url)


# Remove item from cart
def remove_item(request):
    '''Remove the item from the cart'''
    product_id = request.POST.get('product_id')
    cart = request.session.get('cart', {})
    if product_id in cart:
        del cart[product_id]
        request.session['cart'] = cart
        messages.error(request, f'Removed item from your cart')

    return redirect('view_cart')


# Update cart
def update_cart(request):
    '''Update the quantity of a product in the cart'''
    product_id = request.POST.get('product_id')
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if product_id in list(cart.keys()):
        cart[product_id] = quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart

    # Calculate the cart total
    cart_total = Decimal('0.00')
    line_totals = {}
    total_items = 0
    for product_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=product_id)
        cart_total += product.price * quantity
        line_total = quantity * product.price
        line_totals[product_id] = line_total
        total_items += quantity

    # Calculate the delivery and grand total
    if cart_total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = cart_total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - cart_total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + cart_total

    return JsonResponse({'cart_total': cart_total,
                         'grand_total': round(grand_total, 2),
                         'line_totals': line_totals,
                         'total_items': total_items,
                         })
