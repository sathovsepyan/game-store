from django.urls import path
from django.views.generic import TemplateView
from payments.views import get_payment, receive_success_payment, receive_error_payment, receive_cancel_payment

urlpatterns = [
    path('payment/<int:order_pk>/', get_payment, name='payment'),
    path('payment/<uuid:order_code>/success/', receive_success_payment, name='payment_success_view'),
    path('payment/<uuid:order_code>/error/', receive_error_payment, name='payment_error_view'),
    path('payment/<uuid:order_code>/cancel/', receive_cancel_payment, name='payment_cancel_view'),
]
