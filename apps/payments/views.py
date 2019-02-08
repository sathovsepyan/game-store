from django.shortcuts import render


from django.views.generic import FormView

from profiles.forms import SignUpForm


class CheckoutFormView(FormView):
    form_class = 
    template_name = 'checkout.html'
    success_url = '/'
