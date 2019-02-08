from django.urls import path

from games.views import GameDetailView

urlpatterns = [
    path(
        '<int:pk>/',
        GameDetailView.as_view(),
        name='game_detail_view'
    )
]
