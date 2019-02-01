from django.db import models
from django.contrib.auth.models import User

from games.models import Game


class Profile(models.Model):
    ROLES = [
        ('player', 'Player'),
        ('developer', 'Developer'),
    ]
    role = models.CharField(choices=ROLES, max_length=20)
    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE
    )
    games = models.ManyToManyField(Game)

    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'
