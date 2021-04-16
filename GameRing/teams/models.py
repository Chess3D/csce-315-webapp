from django.db import models
from django import forms

# Create your models here.
TEAM_TYPE_CHOICES = [
    ("league", "League of Legends"),
    ("valorant", "Valorant"),
]

class Team(models.Model):
    name = models.CharField("Name", max_length=60)
    game = models.CharField("Game", max_length=31, choices=TEAM_TYPE_CHOICES, default='league')
    ELO = models.BigIntegerField("Hidden ELO", default="500")
    logo = models.ImageField(upload_to='card_images/', default = 'card_images/GameRing.png')