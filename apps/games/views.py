from django.contrib.auth.decorators import login_required
from django.views.generic import DetailView
from django.shortcuts import render, get_object_or_404
from django.core.exceptions import PermissionDenied
from django.db.models import Q
from games.models import Game


class GameDetailView(DetailView):
    model = Game
    template_name = 'games/game_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            purchased_games = self.request.user.profile.games.all()
            context['is_purchased'] = self.object in purchased_games
        context['other_games'] = Game.objects.filter(~Q(id=self.object.id), is_deleted=False)[:6]
        return context


@login_required
def playgame(request, game_id):
    game = get_object_or_404(Game, pk=game_id)
    # check if the user request.user belongs  to the game/profile.
    if game not in request.user.profile.games.all():
        raise PermissionDenied()
    return render(request, 'games/gamecontainer.html', {'game': game})
