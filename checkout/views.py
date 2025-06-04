from decimal import Decimal
from django.shortcuts import (
    render, redirect, reverse, HttpResponse, get_object_or_404
)
from django.contrib import messages
from django.views.decorators.http import require_POST
from .forms import OrderForm
from django.conf import settings
from django.http import JsonResponse
from cart.contexts import cart_contents
from menu.models import MenuItem, Sauce
from .models import Order, OrderLineItem
from profiles.forms import UserProfileForm
from profiles.models import UserProfile
import stripe
import json


@require_POST
def cache_checkout_data(request):
    print("Received POST data:", request.POST)

    try:
        client_secret = request.POST.get('client_secret', '')
        if not client_secret:
            raise ValueError("Missing client_secret in POST data")

        pid = client_secret.split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY

        delivery_method = request.POST.get('delivery_method', 'pickup')
        request.session['delivery_method'] = delivery_method

        username = (
            request.user.username
            if request.user.is_authenticated
            else 'AnonymousUser'
        )

        stripe.PaymentIntent.modify(pid, metadata={
            'cart': json.dumps(request.session.get('cart', {})),
            'save_info': request.POST.get('save_info', 'false'),
            'username': username,
            'delivery_method': delivery_method,
        })
        return HttpResponse(status=200)
    except Exception as e:
        return HttpResponse(content=str(e), status=400)


def create_payment_intent(request):
    if request.method == 'POST':
        delivery_method = request.POST.get('delivery_method', 'pickup')
        request.session['delivery_method'] = delivery_method

        current_cart = cart_contents(request)

        total = float(current_cart['total'])
        delivery = float(current_cart['delivery'])
        grand_total = float(current_cart['grand_total'])

        stripe_total = round(grand_total * 100)

        stripe.api_key = settings.STRIPE_SECRET_KEY
        payment_intent_id = request.session.get('payment_intent_id')

        if payment_intent_id:
            try:
                existing_intent = stripe.PaymentIntent.retrieve(
                    payment_intent_id
                )
                if existing_intent.status == 'succeeded':
                    # Clear the old one — it's already paid
                    del request.session['payment_intent_id']
                    payment_intent_id = None
            except stripe.error.InvalidRequestError:
                payment_intent_id = None

        if payment_intent_id:
            try:
                # Try to update the existing PaymentIntent amount
                intent = stripe.PaymentIntent.modify(
                    payment_intent_id,
                    amount=stripe_total,
                )
            except stripe.error.InvalidRequestError:
                # If update fails, cancel the old intent and create a new one
                try:
                    stripe.PaymentIntent.cancel(payment_intent_id)
                except Exception as e:
                    pass

                intent = stripe.PaymentIntent.create(
                    amount=stripe_total,
                    currency=settings.STRIPE_CURRENCY,
                )
                request.session['payment_intent_id'] = intent.id
        else:
            # Create a new PaymentIntent if none exists
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            request.session['payment_intent_id'] = intent.id

        return JsonResponse({
            'client_secret': intent.client_secret,
            'total': total,
            'delivery': delivery,
            'grand_total': grand_total,
        })

    return JsonResponse({'error': 'Invalid request'}, status=400)


def checkout(request):
    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY
    order = None

    if request.method == 'POST':
        delivery_method = request.POST.get('delivery_method', 'pickup')
        request.session['delivery_method'] = delivery_method

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
            'delivery_method': delivery_method,
        }

        order_form = OrderForm(form_data)

        if order_form.is_valid():
            order = order_form.save(commit=False)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_cart = json.dumps(cart)
            order.delivery_method = delivery_method

            # Set delivery cost before saving
            if delivery_method == 'pickup':
                order.delivery_cost = 0
            else:
                order.delivery_cost = Decimal(
                    request.session.get('delivery_cost', '0.00')
                )

            order.save()

            for key, item_data in cart.items():
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
                            messages.error(
                                request,
                                "Missing sauce. Please review your cart."
                            )
                            order.delete()
                            return redirect(reverse('view_cart'))

                    quantity = item_data.get('quantity', 1)

                    order_line_item = OrderLineItem(
                        order=order,
                        menu_item=menu_item,
                        quantity=quantity,
                        sauce=sauce,
                    )
                    order_line_item.save()

                except MenuItem.DoesNotExist:
                    messages.error(
                        request,
                        "Missing item. Please review your cart."
                    )
                    order.delete()
                    return redirect(reverse('view_cart'))

            order.stripe_pid = pid

            request.session['save_info'] = 'save-info' in request.POST
            return redirect(
                reverse('checkout_success', args=[order.order_number])
            )
        else:
            messages.error(
                request,
                'There was an error with your form. Please try again.'
            )

    else:
        cart = request.session.get('cart', {})
        if not cart:
            messages.error(
                request,
                "There's nothing in your cart at the moment!"
            )
            return redirect(reverse('menu'))

        current_cart = cart_contents(request)
        stripe_total = round(float(current_cart['grand_total']) * 100)

        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.api_key = settings.STRIPE_SECRET_KEY
        payment_intent_id = request.session.get('payment_intent_id')

        if not payment_intent_id:
            intent = stripe.PaymentIntent.create(
                amount=stripe_total,
                currency=settings.STRIPE_CURRENCY,
            )
            request.session['payment_intent_id'] = intent.id
        else:
            try:
                intent = stripe.PaymentIntent.retrieve(payment_intent_id)
            except stripe.error.InvalidRequestError:
                # If somehow the ID is invalid or expired, create a new one
                intent = stripe.PaymentIntent.create(
                    amount=stripe_total,
                    currency=settings.STRIPE_CURRENCY,
                )
                request.session['payment_intent_id'] = intent.id

        if request.user.is_authenticated:
            try:
                profile = UserProfile.objects.get(user=request.user)
                order_form = OrderForm(initial={
                    'full_name': profile.user.get_full_name(),
                    'email': profile.user.email,
                    'phone_number': profile.default_phone_number,
                    'postcode': profile.default_postcode,
                    'town_or_city': profile.default_town_or_city,
                    'street_address1': profile.default_street_address1,
                    'street_address2': profile.default_street_address2,
                    'state': profile.default_state,
                })
            except UserProfile.DoesNotExist:
                order_form = OrderForm()
        else:
            order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing.')

        return render(request, 'checkout/checkout.html', {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
            'order': order,
        })


def checkout_success(request, order_number):
    """
    Handle successful checkouts
    """
    save_info = request.session.get('save_info')
    order = get_object_or_404(Order, order_number=order_number)

    if request.user.is_authenticated:
        try:
            profile = UserProfile.objects.get(user=request.user)
            order.user_profile = profile
            order.save()

            if save_info:
                profile_data = {
                    'default_phone_number': order.phone_number,
                    'default_postcode': order.postcode,
                    'default_town_or_city': order.town_or_city,
                    'default_street_address1': order.street_address1,
                    'default_street_address2': order.street_address2,
                    'default_state': order.state,
                }
                user_profile_form = UserProfileForm(
                    profile_data,
                    instance=profile
                )
                if user_profile_form.is_valid():
                    user_profile_form.save()
        except UserProfile.DoesNotExist:
            pass

    messages.success(
        request,
        f'Order successfully processed! Your order number is {order_number}. '
        f'A confirmation email will be sent to {order.email}.'
    )
    if 'cart' in request.session:
        del request.session['cart']

    if 'payment_intent_id' in request.session:
        del request.session['payment_intent_id']

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }
    return render(request, template, context)
