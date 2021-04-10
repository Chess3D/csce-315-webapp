from django.db import models

class Tournament(models.Model):
    name = models.CharField("Name", max_length=60)
    tournamentType = models.CharField("tournamentType", max_length=255)
    tournamentURL = models.CharField("TournamentURL", max_length=255)
    tournamentDescription = models.CharField("tournamentDescription", max_length=511)
    tournamentType = models.CharField("tournamentType", max_length=255)
    tournamentThirdPlaceMatch = models.BooleanField("tournamentThirdPlaceMatch", default=True)
    tournamentRankedBy = models.CharField("tournamentRankedby", max_length=31)
    tournamentShowRounds = models.BooleanField("tournamentShowRounds", default=True)
    tournamentPrivate = models.BooleanField("tournamentPrivate", default=False)
    tournamentNotifyUserWhenOpen = models.BooleanField("tournamentNotifyUserWhenOpen", default=False)
    tournamentNotifyUserWhenTournyEnd = models.BooleanField("tournamentNotifyUserWhenTournyEnd")
    #tournamentSeqPairings = models.BooleanField("tournamentSeqPairings", default=False)
    tournamentSignUpCap = models.BigIntegerField("tournamentSignUpCap")
    tournamentStartDate = models.DateTimeField("tournamentStartDate")
    #tournamentCheckInDuration = models.BigIntegerField("tournamentCheckInDuration") #in minutes
    tournamentGrandFinalsMod = models.CharField("tournamentGrandFinalsMod", max_length=31)
    
    tournamentGameName = models.CharField("tournamentGameName", max_length=255)
    

    def __str__(self):
        return self.name

