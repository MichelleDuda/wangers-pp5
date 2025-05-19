from django.shortcuts import render, redirect, reverse
from django.contrib import messages
from .forms import OrderForm

# Create your views here.
def checkout(request):
    cart = request.session.get ('cart', {})
    if not cart:
        messages.error(request, "There's nothing in your cart at the moment!")
        return redirect(reverse('menu'))
    
    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51RQSXBD5BVLL0zXK9nGwotI0MQw0ybu5fhuNcyBPHAEbNQgYdnIO6fS1AoMsWBq2cgs0nBgtFgnN14on2a596m9Q00lp4V5pSx',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)