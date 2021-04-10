from django import forms

from tournaments.models import Tournament

class TournamentCreationForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = '__all__'

        widgets = {
           #Text Inputs
           'tournamentURL': forms.TextInput(attrs={'class': 'form-control'}),
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'tournamentDescription': forms.Textarea(attrs={'class': 'form-control'}),

           #Drop down
           'tournamentType': forms.Select(attrs={'class': 'form-control'}),
           'tournamentGameName': forms.Select(attrs={'class': 'form-control'}),
        }