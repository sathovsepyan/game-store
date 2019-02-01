from django.urls import path

from payments.views import CheckoutFormView

urlpatterns = [
    path(
        'checkout/',
        CheckoutFormView.as_view(),
        name='checkout_form_view'
    )
]
