from django.shortcuts import render, redirect, get_object_or_404, reverse, HttpResponse
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
    else:
        cart[key] = {
            'menu_item_id': item_id,
            'quantity': quantity,
            'sauce_id': sauce_id,
        }

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
        else:
            return HttpResponse(status=404)

        request.session['cart'] = cart
        return HttpResponse(status=200)

    except Exception as e:
        print(f"Error: {e}")
        return HttpResponse(status=500)