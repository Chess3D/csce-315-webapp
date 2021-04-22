from django.db import models
from django import forms
from django.contrib.auth.models import User

# Create your models here.
TEAM_TYPE_CHOICES = [
    ("league", "League of Legends"),
    ("valorant", "Valorant"),
]


class Team(models.Model):
    name = models.CharField("Name", max_length=64, unique=True)
    game = models.CharField("Game", max_length=32, choices=TEAM_TYPE_CHOICES, default='league')
    ELO = models.BigIntegerField("Hidden ELO", default="500")
    logo = models.ImageField(upload_to='card_images/', default = 'card_images/GameRing.png')
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class TeamManager(models.Manager):
    use_for_related_fields = True

    def add_player(self, player, team):
        # player.team.add
        team.players.add(user)

    def remove_player(self, user, team):
        team.players.remove(user)


class Player(models.Model):
    username = models.CharField("Name", max_length=64, unique=True)

    user = models.ForeignKey(
        User,
        on_delete=models.DO_NOTHING,
    )

    team = models.ForeignKey(
        Team,
        on_delete=models.DO_NOTHING,
    )

    objects = TeamManager()