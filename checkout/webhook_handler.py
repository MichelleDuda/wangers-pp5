from django.http import HttpResponse
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from .models import Order, OrderLineItem
from menu.models import MenuItem, Sauce
from profiles.models import UserProfile

import stripe
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def _send_confirmation_email(self, order):
        """Send the user a confirmation email"""
        cust_email = order.email
        subject = render_to_string(
            'checkout/confirmation_emails/confirmation_email_subject.txt',
            {'order': order})
        body = render_to_string(
            'checkout/confirmation_emails/confirmation_email_body.txt',
            {'order': order, 'contact_email': settings.DEFAULT_FROM_EMAIL})

        send_mail(
            subject,
            body,
            settings.DEFAULT_FROM_EMAIL,
            [cust_email]
        )

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """Handle the payment_intent.succeeded webhook from Stripe"""
        intent = event.data.object
        pid = intent.id
        cart = json.loads(intent.metadata.cart)
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(intent.latest_charge)

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        delivery_method = intent.metadata.get('delivery_method', 'pickup')

        print(f"Delivery Method Chosen: {delivery_method}")

        # Normalize empty strings in shipping address to None
        if shipping_details and shipping_details.address:
            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None

        # Update profile info if user is logged in and save_info is True
        profile = None
        username = intent.metadata.username
        if username != 'AnonymousUser':
            try:
                profile = UserProfile.objects.get(user__username=username)
                if save_info:
                    profile.default_phone_number = shipping_details.phone
                    profile.default_postcode = (
                        shipping_details.address.postal_code
                    )
                    profile.default_town_or_city = (
                        shipping_details.address.city
                    )
                    profile.default_street_address1 = (
                        shipping_details.address.line1
                    )
                    profile.default_street_address2 = (
                        shipping_details.address.line2
                    )
                    profile.default_county = shipping_details.address.state
                    profile.save()
            except UserProfile.DoesNotExist:
                profile = None

        # Check if order with this Stripe payment intent ID already exists
        order = None
        attempt = 1
        while attempt <= 10:
            try:
                order = Order.objects.get(stripe_pid=pid)
                break
            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order:
            # Order already exists, send confirmation email and exit
            self._send_confirmation_email(order)
            return HttpResponse(
                content=(
                    f'Webhook received: {event["type"]} | SUCCESS: Verified '
                    'order already in database'
                ),
                status=200
            )

        # Create the order if not found
        try:
            order_data = {
                "full_name": shipping_details.name,
                "user_profile": profile,
                "email": billing_details.email,
                "phone_number": shipping_details.phone,
                "original_cart": json.dumps(cart),
                "stripe_pid": pid,
                "grand_total": grand_total,
                "delivery_method": delivery_method,
            }

            if delivery_method == 'delivery':
                order_data.update({
                    "postcode": shipping_details.address.postal_code,
                    "town_or_city": shipping_details.address.city,
                    "street_address1": shipping_details.address.line1,
                    "street_address2": shipping_details.address.line2,
                    "state": shipping_details.address.state,
                })

            order = Order.objects.create(**order_data)

            # Create line items for the order
            for key, item_data in cart.items():
                parts = key.split('_')
                item_id = int(parts[0])
                sauce_id = (
                    int(parts[1])
                    if len(parts) > 1 and parts[1] != 'None'
                    else None
                )
                quantity = item_data['quantity']

                menu_item = MenuItem.objects.get(pk=item_id)
                sauce = Sauce.objects.get(pk=sauce_id) if sauce_id else None

                OrderLineItem.objects.create(
                    order=order,
                    menu_item=menu_item,
                    quantity=quantity,
                    sauce=sauce,
                )

        except Exception as e:
            # If error occurs, delete incomplete order to avoid corrupt data
            if order:
                order.delete()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {e}',
                status=500)

        # Send confirmation email after successful order creation
        self._send_confirmation_email(order)
        return HttpResponse(
            content=(
                f'Webhook received: {event["type"]} | SUCCESS: '
                'Created order in webhook'
            ),
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)
