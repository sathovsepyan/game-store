from django.db import models
from django.contrib.auth.models import User

from games.models import Game


class Score(models.Model):
    game = models.ForeignKey(Game, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    score = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f'{self.user.get_fullname()} - {self.game.title} - {self.score}'
