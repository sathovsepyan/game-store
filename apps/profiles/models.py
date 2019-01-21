from django.db import models

from games.models import Game


class Profile(models.Model):
    ROLES = [
        ('player', 'Player'),
        ('developer', 'Developer'),
    ]
    role = models.CharField(choices=ROLES, max_length=20)
    games = models.ManyToManyField(Game)
