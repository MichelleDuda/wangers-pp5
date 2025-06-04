from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from menu.models import MenuItem, Sauce, AddOn


def cart_contents(request):
    cart_items = []
    total = 0
    product_count = 0
    cart = request.session.get('cart', {})

    for key, item_data in cart.items():
        # Split item_id and sauce_id from the key if a sauce_id exists
        parts = key.strip('_').split('_')

        # Parse item_id
        item_id = int(parts[0])

        # Parse sauce_id if exists
        sauce_id = None
        if len(parts) > 1 and parts[1] not in ('None', ''):
            try:
                sauce_id = int(parts[1])
            except ValueError:
                sauce_id = None

        # Retrieve the menu item and sauce objects
        menu_item = get_object_or_404(MenuItem, pk=item_id)
        sauce = get_object_or_404(Sauce, pk=sauce_id) if sauce_id else None

        print(f"Cart key: {key}, item_id: {item_id}, sauce_id: {sauce_id}")
        print(f"Sauce object: {sauce}")

        quantity = item_data.get('quantity', 1)

        # Calculate Add On Portion
        add_on_ids = item_data.get('add_ons', [])
        add_on_ids = [int(a) for a in add_on_ids] if add_on_ids else []
        add_ons = AddOn.objects.filter(id__in=add_on_ids)
        add_ons_total = sum(add_on.price for add_on in add_ons)

        # Calculate the line total
        line_total = ((quantity * menu_item.price) + add_ons_total)
        print(line_total)
        total += line_total
        product_count += quantity

        cart_items.append({
            'key': key,
            'menu_item_id': item_id,
            'quantity': quantity,
            'menu_item': menu_item,
            'sauce': sauce,
            'add_ons': add_ons,
            'line_total': line_total,
        })

    if 'delivery_method' not in request.session:
        request.session['delivery_method'] = 'delivery'
    delivery_method = request.session.get('delivery_method')

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
