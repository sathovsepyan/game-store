from django.views.generic import TemplateView

from games.models import Game
from django.shortcuts import render, get_object_or_404

# TODO: Move from the main app the 'playgame' method to another app that deals the display of the game.

def playgame(request, game_id):
    obj = get_object_or_404(Game, pk=game_id)
    return  render(request, 'main/gamecontainer.html', {'game': obj})


class IndexPageView(TemplateView):
    template_name = 'main/index.html'
