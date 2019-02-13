from django.http import JsonResponse
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView
from django.core.exceptions import PermissionDenied

from games.models import Game
from scores.models import Score


def save_score(request, game_pk):
    game = get_object_or_404(Game, pk=game_pk)
    if game not in request.user.profile.games.all():
        raise PermissionDenied

    Score.objects.create(
        game=game,
        user=request.user,
        score=request.GET.get('score')
    )

    return JsonResponse({
        'status': 'OK',
    })


class HightScoreView(TemplateView):
    template_name = 'scores/high_score.html'

    def get_high_scores(self):
        high_scores = Score.objects.values(
            'game__id',
            'game__title'
        ).annotate(
            max_score=Max('score')
        ).values(
            'game__id',
            'game__title',
            'user__email',
            'max_score'
        )
        return high_scores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['high_score_list'] = self.get_high_scores()
        return context