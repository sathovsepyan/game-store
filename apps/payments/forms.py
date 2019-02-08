from hashlib import md5

from django import forms
from django.urls import reverse_lazy, reverse
from django.conf import settings

from django.contrib.sites.shortcuts import get_current_site

class PaymentForm(forms.Form):
    amount = forms.DecimalField(label='Amount', max_digits=9, decimal_places=2)
    pid = forms.CharField(max_length=255)
    sid = forms.CharField(max_length=255)
    checksum = forms.CharField(max_length=255, required=False)
    success_url = forms.CharField(max_length=255)
    error_url = forms.CharField(max_length=255)
    cancel_url = forms.CharField(max_length=255)

    def __init__(self, *args, **kwargs):
        order = kwargs.pop('order')
        super().__init__(*args, **kwargs)

        self.fields['amount'].widget.attrs['readonly'] = True
        self.fields['checksum'].widget = forms.HiddenInput()
        self.fields['sid'].widget = forms.HiddenInput()
        self.fields['pid'].widget = forms.HiddenInput()
        self.fields['success_url'].widget = forms.HiddenInput()
        self.fields['error_url'].widget = forms.HiddenInput()
        self.fields['cancel_url'].widget = forms.HiddenInput()

        checksumstr = "pid={}&sid={}&amount={}&token={}".format(
            order.code.hex, settings.PAYMENT_SELLER_ID,
            order.total_amount, settings.PAYMENT_SECRET_KEY)
        m = md5(checksumstr.encode("ascii"))
        checksum = m.hexdigest()
        self.fields['checksum'].initial = checksum
        self.fields['sid'].initial = settings.PAYMENT_SELLER_ID
        self.fields['pid'].initial = order.code.hex
        self.fields['amount'].initial = order.total_amount
        self.fields['success_url'].initial = "{}{}".format("http://127.0.0.1:8000", reverse('payment_success_view', kwargs={'order_code': order.code}))
        self.fields['error_url'].initial = "{}{}".format("http://127.0.0.1:8000", reverse('payment_error_view', kwargs={'order_code': order.code}))
        self.fields['cancel_url'].initial = "{}{}".format("http://127.0.0.1:8000", reverse('payment_cancel_view', kwargs={'order_code': order.code}))
