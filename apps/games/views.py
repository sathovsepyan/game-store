from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied

from games.models import Game


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'


@login_required
def playgame(request, game_id):
    game = get_object_or_404(Game, pk=game_id)    
    # check if the user request.user belongs  to the game/profile.
    if game not in request.user.profile.games.all():
        raise PermissionDenied()

    return  render(request, 'games/gamecontainer.html', {'game': game})