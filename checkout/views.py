from decimal import Decimal
from django.shortcuts import render, redirect, reverse, HttpResponse, get_object_or_404
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import OrderForm
from django.conf import settings
from cart.contexts import cart_contents
from menu.models import MenuItem, Sauce
from .models import Order, OrderLineItem
import stripe
import json

# Create your views here.
@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info'),
            'username': request.user,
            'delivery_method': request.POST.get('delivery_method', 'pickup'),
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order = None

    if request.method == 'POST':
        cart = request.session.get('cart', {})
        
        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
            'phone_number': request.POST['phone_number'],
            'postcode': request.POST.get('postcode', ''),
            'town_or_city': request.POST.get('town_or_city', ''),
            'street_address1': request.POST.get('street_address1', ''),
            'street_address2': request.POST.get('street_address2', ''),
            'state': request.POST.get('state', ''),
            'delivery_method': request.POST.get('delivery_method', 'pickup'),
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.strip_pid = pid
            order.original_bag = json.dumps(cart)
            order.delivery_method = form_data['delivery_method']

            if order.delivery_method == 'pickup':
                order.delivery_cost = 0
            else:
                order.delivery_cost = Decimal(request.session.get('delivery_cost', '0.00'))

            print("Delivery Method Chosen:", order.delivery_method)

            order.save()

            for key, item_data in cart.items():
                # Split item_id and sauce_id from the key if sauce_id exists
                parts = key.split('_')
                if len(parts) == 2:
                    item_id, sauce_id = parts
                    sauce_id = int(sauce_id) if sauce_id != 'None' else None
                else:
                    item_id = parts[0]
                    sauce_id = None
                item_id = int(item_id)

                try:
                    menu_item = MenuItem.objects.get(pk=item_id)
                    sauce = None
                    if sauce_id:
                        try:
                            sauce = Sauce.objects.get(pk=sauce_id)
                        except Sauce.DoesNotExist:
                            messages.error(request, (
                                "Uh-oh! One of your sauces has vanished into thin air! "
                                "We can’t find it in our system—please contact us so we can fix this dip-tastrophe!"
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
                    return redirect(reverse('view_cart'))
                
            order.update_total()

            stripe.api_key = stripe_secret_key
            stripe_total = round(order.grand_total * 100)

            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(reverse('checkout_success', args=[order.order_number]))
        else:
            messages.error(request, 'Uh-oh! Something seems a bit off in your order. \
                Please double check your information so we can get those wings flying your way!')
            
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
        'order': order,
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