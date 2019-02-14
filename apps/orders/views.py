from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

from games.models import Game
from orders.models import Order
from orders.forms import PaymentForm
from main.mixins import LoginRequiredMixin
from django.conf import settings
from hashlib import md5


class CreateOrderView(LoginRequiredMixin, TemplateView):
    model = Order
    form_class = PaymentForm
    success_url = reverse_lazy('purchased_game_view')
    template_name = 'orders/order_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.game = get_object_or_404(Game, pk=kwargs.get('game_pk'))
        # check that player already has that game
        profile = self.request.user.profile
        if self.game in profile.games.all():
            return redirect(
                reverse_lazy('index_page_view')
            )
        # check that developer could not buy the game
        if profile.is_developer:
            games = Game.objects.filter(developer=self.request.user)
            if self.game in games:
                return redirect(
                    reverse_lazy('index_page_view')
                )
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.game
        context['form'] = self.form
        return context

    def get(self, request, *args, **kwargs):
        order = Order.objects.create(
            user=self.request.user,
            total_amount=self.game.price,
            game=self.game
        )

        self.form = PaymentForm(order=order)

        return super().get(request, args, kwargs)


def receive_success_payment(request, order_code):
    pid = request.GET['pid']
    ref = request.GET['ref']
    result = request.GET['result']
    checksum = request.GET['checksum']

    if result != 'success':
        return render(request, 'orders/payment_error.html')

    order = Order.objects.get(code=pid)
    game = Game.objects.get(id=order.game_id)

    checksumstr = 'pid={}&ref={}&result={}&token={}'.format(
            order.code.hex, ref,
            result, settings.PAYMENT_SECRET_KEY)
    m = md5(checksumstr.encode('ascii'))
    originalChecksum = m.hexdigest()

    if originalChecksum != checksum:
        return render(request, 'orders/payment_error.html')

    order.ref = ref
    order.save()

    request.user.profile.games.add(game)
    request.user.save()

    return redirect('purchased_game_view')


def receive_error_payment(request, order_code):
    return render(request, 'payment_error.html')


def receive_cancel_payment(request, order_code):
    order = Order.objects.get(code=order_code)
    return redirect('create_order_view', game_pk=order.game_id)
