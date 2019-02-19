from django.http import JsonResponse
from django.db.models import Max
from django.shortcuts import get_object_or_404
from django.views.generic import TemplateView, ListView
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
        ).order_by('-max_score')
        return high_scores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['high_score_list'] = self.get_high_scores()
        return context


class ScoreListView(TemplateView):
    template_name = 'scores/score_list.html'
    # model = Score

    # def get_queryset(self):
    #     qs = super().get_queryset()
    #     qs = qs.filter(user=self.request.user).order_by('-score')
    #     return qs
    def get_scores_by_user(self):
        high_scores = Score.objects.values(
            'game__id',
            'game__title'
        ).annotate(
            max_score=Max('score')
        ).filter(
            user=self.request.user
        ).values(
            'game__id',
            'game__title',
            'user__email',
            'max_score'
        ).order_by('-max_score')
        return high_scores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['high_score_list'] = self.get_scores_by_user()
        return context

class ScoreGameView(TemplateView):
    template_name = 'scores/score_game.html'

    def get_scores_by_game(self):
        high_scores = Score.objects.values(
            'game__id',
            'game__title'
        ).annotate(
            max_score=Max('score')
        ).filter(
            game=self.kwargs['game_pk']
        ).values(
            'game__id',
            'game__title',
            'user__email',
            'max_score'
        ).order_by('-max_score')
        return high_scores

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['high_score_list'] = self.get_scores_by_game()
        return context