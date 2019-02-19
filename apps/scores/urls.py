from django.urls import path

from scores.views import save_score, HightScoreView, ScoreListView, ScoreGameView

urlpatterns = [
    path('<int:game_pk>/save/', save_score, name='save_game_score'),
    path('high-score/', HightScoreView.as_view(), name='high_score_view'),
    path('', ScoreListView.as_view(), name='score_list_view'),
    path('<int:game_pk>/', ScoreGameView.as_view(), name='score_by_game'),
]
