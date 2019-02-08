from django.shortcuts import render, get_object_or_404
from payments.forms import PaymentForm
from orders.models import Order
from django.conf import settings
from django.http import HttpResponseRedirect, HttpResponse
from hashlib import md5
from decimal import *
import requests

def get_payment(request, order_pk):
    order = get_object_or_404(Order, pk=order_pk)
    form = PaymentForm(order=order)

    return render(request, 'payment.html', {'form': form})


def receive_success_payment(request, order_code):
    return HttpResponse('OK')


def receive_error_payment(request, order_code):
    return HttpResponse('Error')


def receive_cancel_payment(request, order_code):
    return HttpResponse('Cancel')
