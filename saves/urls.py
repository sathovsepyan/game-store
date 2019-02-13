from django.urls import path
from saves import views

urlpatterns = [
    path('<int:game_id>/save', views.savegame),
    path('<int:game_id>/load/', views.loadgame),
]
