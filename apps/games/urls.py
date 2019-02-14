from django.urls import path

from games.views import GameDetailView

from games import views

urlpatterns = [
    path(
        '<int:pk>/',
        GameDetailView.as_view(),
        name='game_detail_view'
    ),
    path('<int:game_id>/play/', views.playgame, name='play_game_view'),
]

