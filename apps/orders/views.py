from django.views.generic import CreateView
from django.urls import reverse_lazy

from games.models import Game
from orders.models import Order
from orders.forms import CreateOrderForm
from main.mixins import LoginRequiredMixin


class CreateOrderView(LoginRequiredMixin, CreateView):
    model = Order
    form_class = CreateOrderForm
    success_url = reverse_lazy('purchased_game_view')

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
        self.request.user.profile.games.add(self.game)
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.game
        return context
