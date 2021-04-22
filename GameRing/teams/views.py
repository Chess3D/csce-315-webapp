from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseNotFound
from django.http import HttpResponse

from .models import TeamManager, Team
from .forms import TeamCreationForm
from django.views.generic import ListView
from django.contrib.auth.models import User

# from rest_framework.decorators import api_view

def teams(request):
    
    context = {
        'teams': Team.objects.all()
    }

    return render(request, 'teams/teams.html')


def about_team(request, team_id):
    
    context = {
        'team_id': team_id,
        'team': Team.objects.get(id=team_id)
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


def join_team(request, team_id):
    context = {
        'team_id': team_id,
    }

    team = Team.objects.get(id=team_id)
    user = request.user

    TeamManager.add_player(request, user, team)

    return about_team(request, team_id)


class TeamListView(ListView):
    model = Team
    template_name = 'teams/teams.html'
    context_object_name = 'teams'