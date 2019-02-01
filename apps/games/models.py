from django.db import models
from django.contrib.auth.models import User

from categories.models import Category


class Game(models.Model):
    STATUS = [
        ('active', 'Active'),
        ('inactive', 'Inactive'),
        ('review', 'On review')
    ]

    url = models.URLField()
    title = models.CharField(max_length=255)
    description = models.TextField()
    price = models.PositiveIntegerField()
    category = models.ManyToManyField(Category)
    developer = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(choices=STATUS, max_length=20)
    is_deleted = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Game'
        verbose_name_plural = 'Games'
        ordering = ['created']