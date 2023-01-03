from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from shop.models import Product


def cart_contents(request):
    """Ensures that the cart contents are available when rendering every page"""

    # Initialise the cart items, total, product count, and delivery variables
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    # Calculate the cart total, product count, and line total - for each item
    # in the cart, add the quantity to the product count, and the line total
    # to the total
    for item_id, quantity in cart.items():
        product = get_object_or_404(Product, pk=item_id)
        total += Decimal(quantity) * product.price
        product_count += quantity
        line_total = quantity * product.price
        cart_items.append({'item_id': item_id, 'quantity': quantity,
                           'product': product, 'line_total': line_total})

    # Calculate the delivery cost
    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    # Create the context dictionary
    context = {
        'cart_items': cart_items,
        'total': total,
        'grand_total': round(grand_total, 2),
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
    }

    return context
