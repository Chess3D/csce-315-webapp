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

class Tournament(models.Model):
    name = models.CharField("Name", max_length=60)
    tournamentGameName = models.CharField("Game", max_length=31, choices=TOURNAMENT_GAME_CHOICES, default='league-oflegends')
    tournamentType = models.CharField("Type of Tournament", max_length=31, choices=TOURNAMENT_TYPE_CHOICES, default='round-robin')
    tournamentGrandFinalsMod = models.CharField("Type of Tournament", max_length=31, choices=GRAND_FINAL_CHOICES, default='single-match')
    tournamentURL = models.CharField("Tournament URL", max_length=255, default='coolmathgames.com')
    #tournamentRankedBy = models.CharField("tournament Ranked by", max_length=31)
    tournamentSignUpCap = models.BigIntegerField("Sign Up Capacity")
    tournamentStartDate = models.DateTimeField("Start Date")
    tournamentThirdPlaceMatch = models.BooleanField("Third Place Match", default=True)
    tournamentShowRounds = models.BooleanField("Show Rounds", default=True)
    tournamentPrivate = models.BooleanField("Private", default=False)
    tournamentNotifyUserWhenOpen = models.BooleanField("Notify User When Open", default=False)
    tournamentNotifyUserWhenTournyEnd = models.BooleanField("Notify User When Ended")
    #tournamentSeqPairings = models.BooleanField("tournamentSeqPairings", default=False)
    #tournamentCheckInDuration = models.BigIntegerField("tournamentCheckInDuration") #in minutes
    tournamentDescription = models.CharField("Description", max_length=511)
    image = models.ImageField(upload_to='card_images/', default = 'card_images/GameRing.png')
    creator = models.OneToOneField(User, on_delete=models.CASCADE, default="")
    

    def __str__(self):
        return self.name

