from django.urls import path
from . import views
from .webhooks import webhook

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path(
        'checkout_success/<order_number>/',
        views.checkout_success,
        name='checkout_success'
    ),
    path(
        'cache_checkout_data/',
        views.cache_checkout_data,
        name='cache_checkout_data'
    ),
    path(
        'create-payment-intent/',
        views.create_payment_intent,
        name='create_payment_intent'
    ),
    path('wh/', webhook, name='webhook'),
]
