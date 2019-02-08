from django.urls import path

from orders.views import CreateOrderView


urlpatterns = [
    path(
        'create/game/<int:game_pk>/',
        CreateOrderView.as_view(),
        name='create_order_view'
    )
]
