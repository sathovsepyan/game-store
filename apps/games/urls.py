from django.urls import path

from games.views import CreateGameView

urlpatterns = [
    path(
        'create/',
        CreateGameView.as_view(),
        name='create_game_view'
    )
]
