from django.db import models

from games.models import Game
from django.contrib.auth.models import User

# var savedGame = {
#     messageType: "LOAD",
#     gameState: {
#         playerItems: [
#             "Sword",
#             "Wizard Hat"
#         ],
#         score: 506.0 // Float
#     }
# };

class Save(models.Model):
    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    gamestate = models.TextField(null=True)

    class Meta:
        verbose_name = 'Save'
        verbose_name_plural = 'Saves'
        ordering = ['user']
