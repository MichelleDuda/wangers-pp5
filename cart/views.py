from django.shortcuts import render, redirect

# Create your views here.

def view_cart(request):
    ''' A view to retrun the shopping cart '''
    
    return render(request, 'cart/cart.html')


def add_to_cart(request, item_id):
    ''' A view to add a quanity of a menu item to the shopping cart'''

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    cart = request.session.get('cart', {})

    if item_id in list(cart.keys()):
        cart[item_id] += quantity
    else:
        cart[item_id] = quantity

    request.session['cart'] = cart
    print(request.session['cart'])
    return redirect(redirect_url)


