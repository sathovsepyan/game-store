from django.urls import path

from games.views import CreateGameView, GameListView, GameDetailView

urlpatterns = [
    path(
        'create/',
        CreateGameView.as_view(),
        name='create_game_view'
    ),

    path(
        'list/',
        GameListView.as_view(),
        name='game_list_view'
    ),

    path(
        '<int:pk>',
        GameDetailView.as_view(),
        name='game_detail_view'
    )
]
