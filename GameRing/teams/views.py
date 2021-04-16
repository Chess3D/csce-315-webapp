from django.shortcuts import render
from django.http import HttpResponse

from .models import Team
from .forms import TeamCreationForm
# from django.views.generic import ListView
# from rest_framework.decorators import api_view

def teams(request):
    return render(request, 'teams/teams.html')

def create(request):
    form = TeamCreationForm()

    if request.method == 'POST':
        form = TeamCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('create')

    return render(request, 'teams/create_team.html', {'form': form})