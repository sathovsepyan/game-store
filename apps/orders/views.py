from django.views.generic import CreateView

from games.models import Game
from orders.models import Order
from orders.forms import CreateOrderForm


class CreateOrderView(CreateView):
    model = Order
    form_class = CreateOrderForm
    success_url = '/'

    def dispatch(self, request, *args, **kwargs):
        self.game = Game.objects.get(id=kwargs.get('game_pk'))
        return super().dispatch(request, *args, **kwargs)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        initial = {
            'game': self.game,
            'user': self.request.user,
            'total_amount': self.game.price

        }
        kwargs['initial'] = initial
        return kwargs

    def form_valid(self, form):
        self.user.profile.games.add(self.game)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)