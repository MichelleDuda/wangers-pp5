from decimal import Decimal
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from menu.models import MenuItem

# Create your views here.

def view_cart(request):
    ''' A view to retrun the shopping cart '''
    
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    ''' A view to add a quanity of a menu item to the shopping cart'''

    menu_item = get_object_or_404(MenuItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    sauce_id = request.POST.get ('sauce', None)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    key = f"{item_id}_{sauce_id}" if sauce_id else str(item_id)

    if key in cart:
        cart[key]['quantity'] += quantity
        messages.success(request, f'Updated {menu_item.name} quantity')
    else:
        cart[key] = {
            'menu_item_id': item_id,
            'quantity': quantity,
            'sauce_id': sauce_id,
        }
        messages.success(request, f'Added {menu_item.name} to your cart')

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


def adjust_cart(request, item_id):
    ''' A view to adjust the quanity of a menu item to the shopping cart'''

    menu_item = get_object_or_404(MenuItem, pk=item_id)
    quantity = int(request.POST.get('quantity'))
    sauce_id = request.POST.get ('sauce', None)
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    key = f"{item_id}_{sauce_id}" if sauce_id else str(item_id)

    if key in cart:
        if quantity > 0:
            cart[key]['quantity'] = quantity
            messages.success(request, f'Updated {menu_item.name} quantity')
        else:
            del cart[key]
            if not cart[key]:
                cart.pop(key)

    request.session['cart'] = cart
    return redirect(reverse('cart'))


def remove_from_cart(request, item_id):
    ''' A view to delete a line item from the shopping cart '''

    item_parts = item_id.split('_')
    menu_item_id = item_parts[0]
    sauce_id = item_parts[1] if len(item_parts) > 1 else None

    try:
        menu_item = get_object_or_404(MenuItem, pk=menu_item_id)
        cart = request.session.get('cart', {})
        key = f"{menu_item_id}_{sauce_id}" if sauce_id else str(menu_item_id)

        if key in cart:
            del cart[key]
            messages.success(request, f'Removed {menu_item.name} from cart')
        else:
            return HttpResponse(status=404)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        messages.error(f"Error removing item: {e}")
        return HttpResponse(status=500)
    

@require_POST
def update_delivery_method(request):
    """Update delivery cost based on selected delivery method at checkout."""
    method = request.POST.get('delivery_method', 'pickup')
    cart = request.session.get('cart', {})
    total = 0

    # Calculate total cart value
    for key, item_data in cart.items():
        parts = key.split('_')
        item_id = int(parts[0])
        quantity = item_data.get('quantity', 1)

        try:
            menu_item = MenuItem.objects.get(pk=item_id)
            total += quantity * menu_item.price
        except MenuItem.DoesNotExist:
            continue 

    # Determine delivery cost
    if method == 'pickup':
        delivery_cost = 0
    else:
        if total < settings.FREE_DELIVERY_THRESHOLD:
            delivery_cost = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        else:
            delivery_cost = Decimal('0.00')

    # Store values in session
    request.session['delivery_method'] = method
    request.session['delivery_cost'] = float(delivery_cost)

    return JsonResponse({
        'success': True,
        'delivery_method': method,
        'delivery_cost': str(delivery_cost),
    })