from django.views.generic import CreateView, ListView, DetailView
from django.http import HttpResponseRedirect

from games.models import Game
from games.forms import CreateGameForm


class CreateGameView(CreateView):
    model = Game
    form_class = CreateGameForm
    template_name = 'games/create_game.html'
    success_url = '/'

    def form_valid(self, form):
        game = form.save(commit=False)
        game.developer = self.request.user
        self.object = form.save()
        return HttpResponseRedirect(self.get_success_url())


class GameListView(ListView):
    model = Game
    template_name = 'games/game_list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = qs.filter(developer=self.request.user)
        return qs


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
