from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import Team
from .forms import TeamCreationForm
from django.views.generic import ListView

# from rest_framework.decorators import api_view

def teams(request):
    context = {
        'teams': Team.objects.all()
    }

    return render(request, 'teams/teams.html')

def about_team(request, team_id):
    context = {
        'team_id': team_id,
        'team': Team.objects.all()
    }

    return render(request, 'teams/about_team.html', context)

def create(request):
    form = TeamCreationForm()

    if request.method == 'POST':
        form = TeamCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('create')

    return render(request, 'teams/create_team.html', {'form': form})


class TeamListView(ListView):
    model = Team
    template_name = 'teams/teams.html'
    context_object_name = 'teams'