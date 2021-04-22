from django import forms

from tournaments.models import Tournament

class TournamentCreationForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = (
        'name', 
        'tournamentGameName', 
        'tournamentType', 
        'tournamentGrandFinalsMod', 
        'tournamentSignUpCap', 
        'tournamentStartDate', 
        'tournamentThirdPlaceMatch', 
        'tournamentShowRounds', 
        'tournamentPrivate', 
        'tournamentNotifyUserWhenOpen', 
        'tournamentNotifyUserWhenTournyEnd',
        'tournamentDescription',
        'image',
        #'creator',
        )

        widgets = {
           #Text Inputs
           'tournamentURL': forms.TextInput(attrs={'class': 'form-control'}),
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'tournamentDescription': forms.Textarea(attrs={'class': 'form-control'}),

           #Drop down
           'tournamentType': forms.Select(attrs={'class': 'form-control'}),
           'tournamentGameName': forms.Select(attrs={'class': 'form-control'}),
           'tournamentGrandFinalsMod': forms.Select(attrs={'class': 'form-control'}),
        }

class TournamentJoinForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = (
            'teams',
        )