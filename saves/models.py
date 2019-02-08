from django.db import models

from games.models import Game
from users.models import User

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
    game = models.ForeignKey(Game)
    user = models.ForeignKey(User)
    gamestate = models.TextField(null=True)

    class Meta:
        verbose_name = 'Save'
        verbose_name_plural = 'Saves'
        ordering = ['user']
