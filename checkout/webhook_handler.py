from django.http import HttpResponse
from .models import Order, OrderLineItem
from menu.models import MenuItem, Sauce

import stripe
import json
import time


class StripeWH_Handler:
    """Handle Stripe webhooks"""

    def __init__(self, request):
        self.request = request

    def handle_event(self, event):
        """
        Handle a generic/unknown/unexpected webhook event
        """
        return HttpResponse(
            content=f'Unhandled webhook received: {event["type"]}',
            status=200)

    def handle_payment_intent_succeeded(self, event):
        """
        Handle the payment_intent.succeeded webhook from Stripe
        """
        intent = event.data.object
        pid = intent.id
        cart = json.loads(intent.metadata.cart)
        save_info = intent.metadata.save_info

        stripe_charge = stripe.Charge.retrieve(
            intent.latest_charge
        )

        billing_details = stripe_charge.billing_details
        shipping_details = intent.shipping
        grand_total = round(stripe_charge.amount / 100, 2)

        delivery_method = intent.metadata.get('delivery_method', 'pickup')

        print(f"Delivery Method Chosen: {delivery_method}")

        if shipping_details:
            for field, value in shipping_details.address.items():
                if value == "":
                    shipping_details.address[field] = None

        order_exists = False
        attempt = 1
        while attempt <= 5:
            try:
                order_filter = {
                    "full_name__iexact": shipping_details.name,
                    "email__iexact": billing_details.email,
                    "phone_number__iexact": shipping_details.phone,
                    "grand_total": grand_total,
                    "original_cart": json.dumps(cart),
                    "stripe_pid": pid,
                }

                if delivery_method == 'delivery':
                    order_filter.update({
                        "postcode__iexact": shipping_details.address.postal_code,
                        "town_or_city__iexact": shipping_details.address.city,
                        "street_address1__iexact": shipping_details.address.line1,
                        "street_address2__iexact": shipping_details.address.line2,
                        "state__iexact": shipping_details.address.state,
                    })

                order = Order.objects.get(**order_filter)
                order_exists = True
                break

            except Order.DoesNotExist:
                attempt += 1
                time.sleep(1)

        if order_exists:
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | SUCCESS: Verified order already in database',
                status=200)

        try:
            order_data = {
                "full_name": shipping_details.name,
                "email": billing_details.email,
                "phone_number": shipping_details.phone,
                "original_cart": json.dumps(cart),
                "stripe_pid": pid,
                "grand_total": grand_total,
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

            for key, item_data in cart.items():
                parts = key.split('_')
                item_id = int(parts[0])
                sauce_id = int(parts[1]) if len(parts) > 1 and parts[1] != 'None' else None
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
            if 'order' in locals():
                order.delete()
            return HttpResponse(
                content=f'Webhook received: {event["type"]} | ERROR: {e}',
                status=500)

        return HttpResponse(
            content=f'Webhook received: {event["type"]} | SUCCESS: Created order in webhook',
            status=200)

    def handle_payment_intent_payment_failed(self, event):
        """
        Handle the payment_intent.payment_failed webhook from Stripe
        """
        return HttpResponse(
            content=f'Webhook received: {event["type"]}',
            status=200)