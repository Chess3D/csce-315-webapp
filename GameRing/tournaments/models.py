from django.db import models
from django import forms

TOURNAMENT_TYPE_CHOICES= [
    ('round-robin', 'Round Robin'),
    ('single-elimination', 'Single Elimination'),
    ('double-Elimination', 'Double Elimination'),
]

TOURNAMENT_GAME_CHOICES = [
    ('league-of-legends', 'League of Legends'),
    ('valorant', 'Valorant'),
]

class Tournament(models.Model):
    name = models.CharField("Name", max_length=60)
    tournamentGameName = models.CharField("Game", max_length=30, choices=TOURNAMENT_GAME_CHOICES)
    tournamentType = models.CharField("Type of Tournament", max_length=30, choices=TOURNAMENT_TYPE_CHOICES)
    tournamentURL = models.CharField("Tournament URL", max_length=255)
    tournamentRankedBy = models.CharField("tournament Ranked by", max_length=31)
    tournamentSignUpCap = models.BigIntegerField("Sign Up Capacity")
    tournamentStartDate = models.DateTimeField("Start Date")
    tournamentThirdPlaceMatch = models.BooleanField("Third Place Match", default=True)
    tournamentShowRounds = models.BooleanField("Show Rounds", default=True)
    tournamentPrivate = models.BooleanField("Private", default=False)
    tournamentNotifyUserWhenOpen = models.BooleanField("Notify User When Open", default=False)
    tournamentNotifyUserWhenTournyEnd = models.BooleanField("Notify User When Ended")
    #tournamentSeqPairings = models.BooleanField("tournamentSeqPairings", default=False)
    #tournamentCheckInDuration = models.BigIntegerField("tournamentCheckInDuration") #in minutes
    tournamentGrandFinalsMod = models.CharField("Grand Finals Mod", max_length=31)
    tournamentDescription = models.CharField("Description", max_length=511)
    

    def __str__(self):
        return self.name

