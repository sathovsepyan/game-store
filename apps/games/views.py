from django.views.generic import DetailView

from games.models import Game


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'
