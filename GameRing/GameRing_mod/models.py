from django.db import models
from django import forms
from django.contrib.auth.models import User

TOURNAMENT_TYPE_CHOICES= [
    ('round-robin', 'Round Robin'),
    ('single-elimination', 'Single Elimination'),
    ('double-Elimination', 'Double Elimination'),
]

TOURNAMENT_GAME_CHOICES = [
    ('league-of-legends', 'League of Legends'),
    ('valorant', 'Valorant'),
]

GRAND_FINAL_CHOICES = [
    ('single-match', 'Single Match'),
    ('skip', 'Skip'),
]


TEAM_TYPE_CHOICES = [
    ("league", "League of Legends"),
    ("valorant", "Valorant"),
]


class Team(models.Model):
    name = models.CharField("name", max_length=64, unique=True)
    game = models.CharField("game", max_length=32, choices=TEAM_TYPE_CHOICES, default='league')
    ELO = models.BigIntegerField("Hidden ELO", default="500")
    logo = models.ImageField(upload_to='card_images/', default = 'card_images/GameRing.png')
    players = models.ManyToManyField(User)

    def __str__(self):
        return self.name


class TeamManager(models.Manager):
    use_for_related_fields = True

    def add_player(self, player, team):
        # player.team.add
        team.players.add(User)

    def remove_player(self, user, team):
        team.players.remove(user)


class Tournament(models.Model):
    name = models.CharField("name", max_length=60)
    game_name = models.CharField("game_name", max_length=31, choices=TOURNAMENT_GAME_CHOICES, default='league-of-legends')
    tournament_type = models.CharField("tournament_type", max_length=31, choices=TOURNAMENT_TYPE_CHOICES, default='round-robin')
    grand_finals_modifier = models.CharField("grand_finals_modifier", max_length=31, choices=GRAND_FINAL_CHOICES, default='single-match')
    url = models.CharField("url", max_length=255, default='coolmathgames.com')
    signup_cap = models.BigIntegerField("signup_cap")
    start_at = models.DateTimeField("start_at")
    hold_third_place_match = models.BooleanField("hold_third_place_match", default=True)
    show_rounds = models.BooleanField("show_rounds", default=True)
    description = models.CharField("description", max_length=511)
    image = models.ImageField(upload_to='card_images/', default = 'card_images/GameRing.png')
    creator = models.OneToOneField(User, on_delete=models.CASCADE)
    teams = models.ForeignKey(Team, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.name


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