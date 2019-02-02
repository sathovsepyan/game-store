from django.urls import path

from games.developers import (
    DeveloperGameListView,
    CreateGameView,
    DeleteGameView,
    UpdateGameView,
    DeveloperDashBoard,
    GameSalesDetailsView
)

urlpatterns = [
    path(
        'games/create/',
        CreateGameView.as_view(),
        name='create_game_view'
    ),

    path(
        'games/',
        DeveloperGameListView.as_view(),
        name='game_list_view'
    ),

    path(
        'games/<int:pk>/update/',
        UpdateGameView.as_view(),
        name='game_update_view'
    ),

    path(
        'games/<int:pk>/delete/',
        DeleteGameView.as_view(),
        name='game_delete_view'
    ),

    path(
        '',
        DeveloperDashBoard.as_view(),
        name='developer_dashboard_view'
    ),

    path(
        'games/<int:game_pk>/sales/',
        GameSalesDetailsView.as_view(),
        name='developers_game_sales_details'
    )
]
