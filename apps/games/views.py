from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404

from games.models import Game


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'


@login_required
def playgame(request, game_id):
    obj = get_object_or_404(Game, pk=game_id)    
    return  render(request, 'games/gamecontainer.html', {'game': obj})