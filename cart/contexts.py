from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import MenuItem, Sauce


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for key, item_data in cart.items():
        # Split item_id and sauce_id from the key if a sauce_id exists
        parts = key.split('_')
        if len(parts) == 2:
            item_id, sauce_id = parts
            sauce_id = int(sauce_id) if sauce_id != 'None' else None
        else:
            item_id = parts[0]
            sauce_id = None
        item_id = int(item_id)

        # Retrieve the menu item and sauce objects
        menu_item = get_object_or_404(MenuItem, pk=item_id)
        sauce = get_object_or_404(Sauce, pk=sauce_id) if sauce_id else None

        # Calculate the line total
        quantity = item_data.get('quantity', 1)
        line_total = quantity * menu_item.price
        total += line_total
        product_count += quantity

        cart_items.append({
            'key': key,
            'menu_item_id': item_id,
            'quantity': quantity,
            'menu_item': menu_item,
            'sauce': sauce,
            'line_total': line_total,
        })

    delivery_method = request.session.get('delivery_method', 'delivery')

    if delivery_method == 'pickup':
        delivery = Decimal('0.00')
        free_delivery_delta = Decimal('0.00')
    else:
        free_delivery_threshold = Decimal(settings.FREE_DELIVERY_THRESHOLD)
        standard_delivery_percentage = Decimal(
            settings.STANDARD_DELIVERY_PERCENTAGE
        )

        if total < free_delivery_threshold:
            delivery = total * (standard_delivery_percentage / 100)
            free_delivery_delta = free_delivery_threshold - total
        else:
            delivery = Decimal('0.00')
            free_delivery_delta = Decimal('0.00')

    grand_total = total + delivery

    context = {
        'cart_items': cart_items,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': Decimal(settings.FREE_DELIVERY_THRESHOLD),
        'grand_total': grand_total,
        'delivery_method': delivery_method,
    }

    return context
