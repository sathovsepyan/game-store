from django.urls import path
from saves import views

urlpatterns = [
    path('savegame/<int:game_id>/<int:user_id>', views.savegame),
]
