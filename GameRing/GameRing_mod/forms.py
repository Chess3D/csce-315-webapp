from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from GameRing_mod.models import Tournament, Team, Player


class SignUpForm(UserCreationForm):
    # email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

        widgets = {
           'username': forms.TextInput(attrs={'class': 'form-control', 'autocomplete': 'off'}),
           'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class TournamentCreationForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = (
        'name', 
        'game_name', 
        'tournament_type', 
        'grand_finals_modifier', 
        'signup_cap', 
        'start_at', 
        'hold_third_place_match', 
        'show_rounds',
        'description',
        'image',
        #'creator',
        )

        widgets = {
           #Text Inputs
           'url': forms.TextInput(attrs={'class': 'form-control'}),
           'name': forms.TextInput(attrs={'class': 'form-control'}),
           'description': forms.Textarea(attrs={'class': 'form-control'}),

           #Drop down
           'tournament_type': forms.Select(attrs={'class': 'form-control'}),
           'game_name': forms.Select(attrs={'class': 'form-control'}),
           'grand_finals_modifier': forms.Select(attrs={'class': 'form-control'}),
        }

class TournamentJoinForm(forms.ModelForm):
    class Meta:
        model = Tournament
        fields = (
            'teams',
        )

class TeamCreationForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = (
        'name',
        'game',
        'logo',
        )

        widgets = {
           #Text Inputs
           'name': forms.TextInput(attrs={'class': 'form-control'}),

           #Drop down
           'game': forms.Select(attrs={'class': 'form-control'}),
        }
