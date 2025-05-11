from django.shortcuts import render, redirect, get_object_or_404
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
