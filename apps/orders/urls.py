from django.urls import path

from orders.views import CreateOrderView, receive_success_payment, receive_cancel_payment, receive_error_payment


urlpatterns = [
    path(
        'create/game/<int:game_pk>/',
        CreateOrderView.as_view(),
        name='create_order_view'
    ),
    path('order/<uuid:order_code>/success/', receive_success_payment, name='payment_success_view'),
    path('order/<uuid:order_code>/error/', receive_error_payment, name='payment_error_view'),
    path('order/<uuid:order_code>/cancel/', receive_cancel_payment, name='payment_cancel_view'),
]
