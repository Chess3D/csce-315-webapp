from rest_framework import serializers
from .models import TeamMembers
from .models import Team

class TournamentSerializer(serializers.ModelSerializer):
    Tournament = serializers.RelatedField(many=True)

    class Meta:
        model = Tournament
        fields = (
        'tournamentID',
        'tournamentType', 
        'tournamentURL', 
        'tournamentDescrption', 
        'tournamentType', 
        'tournamentThirdPlaceMatch', 
        'tournamentRankedBy', 
        'tournamentShowRounds', 
        'tournamentPrivate', 
        'tournamentNotifyUserWhenOpen', 
        'tournamentNotifyUserWhenTournyEnd', 
        'tournamentSeqPairings', 
        'tournamentSignUpCap', 
        'tournamentStartDate', 
        'tournamentCheckInDuration', 
        'tournamentGrandFinalsMod',
        'tournamentGameName'
        )