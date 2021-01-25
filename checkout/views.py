from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    bag = request.session.get('bag', {})
    if not bag:
        messages.error(request, "There's nothing in your bag at the minute")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51IDcERKBTecb2BhiyhQgAxXamUTTNBaO4scYLCIaZnHjbb9fYxJ472qqskVZiaJbp66qqxqr4rVbK4a0J88uGrd700X7IpDUEa',
        'client_secret': 'test client',
    }

    return render(request, template, context)