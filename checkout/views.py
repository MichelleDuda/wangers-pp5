from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from .forms import OrderForm
from django.conf import settings
from cart.contexts import cart_contents
from menu.models import MenuItem, Sauce
from .models import Order, OrderLineItem
import stripe

# Create your views here.
def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST['postcode'],
            'town_or_city': request.POST['town_or_city'],
            'street_address1': request.POST['street_address1'],
            'street_address2': request.POST['street_address2'],
            'state': request.POST['state'],
        }
        order_form = OrderForm(form_data)
        if order_form.is_valid():
            order = order_form.save()
            for key, item_data in cart.items():
                # Split item_id and sauce_id from the key
                item_id, sauce_id = key.split('_')
                item_id = int(item_id)
                sauce_id = int(sauce_id) if sauce_id != 'None' else None

                try:
                    menu_item = MenuItem.objects.get(pk=item_id)
                    sauce = None
                    if sauce_id:
                        try:
                            sauce = Sauce.objects.get(pk=sauce_id)
                        except Sauce.DoesNotExist:
                            messages.error(request, (
                                "Uh-oh! One of the sauces in your cart is missing from our system. "
                                "Please contact support for help!"
                            ))
                            order.delete()
                            return redirect(reverse('view_bag'))
                    quantity = item_data.get('quantity', 1)

                    order_line_item = OrderLineItem(
                        order=order,
                        menu_item=menu_item,
                        quantity=quantity,
                        sauce=sauce,
                    )
                    order_line_item.save()

                except MenuItem.DoesNotExist:
                    messages.error(request, (
                        "Uh-oh! One of the items in your cart flew the coop! "
                        "Looks like we couldn’t find it in our system. " 
                        "Give us a call and we’ll help you track down that runaway wing!")
                    )
                    order.delete()
                    return redirect(reverse('view_bag'))

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'There was an error with your form. \
                Please double check your information.')
            
    else:  
        cart = request.session.get ('cart', {})
        if not cart:
            messages.error(request, "There's nothing in your cart at the moment!")
            return redirect(reverse('menu'))
        
        current_cart = cart_contents(request)
        total = current_cart['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )
        
        order_form = OrderForm()

    if not stripe_public_key:
        messages.warning(request, 'Stripe public key is missing. Did you forget to set it in your environment?')

    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': stripe_public_key,
        'client_secret': intent.client_secret,
    }

    return render(request, template, context)

def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')
    
    if 'cart' in request.session:
        del request.session['cart']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)