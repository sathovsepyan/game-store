from django.http import HttpResponseRedirect
from django.core.exceptions import PermissionDenied
from django.views.generic import (
    CreateView,
    ListView,
    DeleteView,
    UpdateView,
    TemplateView
)
from django.urls import reverse_lazy
from django.db.models import Count

from games.models import Game
from games.forms import CreateGameForm
from games.mixins import CheckGameOwnerPermission, CheckDevelopPermission
from main.mixins import LoginRequiredMixin
from orders.models import Order


class CreateGameView(LoginRequiredMixin, CheckDevelopPermission, CreateView):
    model = Game
    form_class = CreateGameForm
    template_name = 'games/create_game.html'
    success_url = reverse_lazy('game_list_view')

    def form_valid(self, form):
        game = form.save(commit=False)
        game.developer = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class DeleteGameView(
    LoginRequiredMixin,
    CheckGameOwnerPermission,
    CheckDevelopPermission,
    DeleteView
):
    queryset = Game.objects.filter(is_deleted=False)
    success_url = reverse_lazy('game_list_view')

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        success_url = self.get_success_url()
        self.object.is_deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)


class UpdateGameView(
    LoginRequiredMixin,
    CheckGameOwnerPermission,
    CheckDevelopPermission,
    UpdateView
):
    queryset = Game.objects.filter(is_deleted=False)
    form_class = CreateGameForm
    success_url = reverse_lazy('game_list_view')


class DeveloperDashBoard(LoginRequiredMixin, CheckDevelopPermission, TemplateView):
    template_name = 'games/developer_dashboard.html'

    def get_games_report(self):
        game_sold = Order.objects.filter(
            game__developer=self.request.user
        ).values(
            'game__title', 'game__id'
        ).annotate(
            gm_count=Count('game__title')
        )
        return game_sold

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({'games_stat': self.get_games_report()})
        return context


class DeveloperGameListView(LoginRequiredMixin, CheckDevelopPermission, ListView):
    queryset = Game.objects.filter(is_deleted=False)
    template_name = 'games/game_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(developer=self.request.user)
        return qs


class GameSalesDetailsView(LoginRequiredMixin, CheckDevelopPermission, ListView):
    model = Order
    template_name = 'games/game_sales_details.html'

    def dispatch(self, request, *args, **kwargs):
        self.game = Game.objects.get(pk=self.kwargs.get('game_pk'))
        if self.game.developer != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(game=self.game, game__developer=self.request.user)
        return qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['game'] = self.game
        return context
