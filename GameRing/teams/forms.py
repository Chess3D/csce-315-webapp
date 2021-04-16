from django import forms
from .models import Team

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