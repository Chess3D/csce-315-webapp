from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import ListView

from GameRing_mod.forms import SignUpForm, TeamCreationForm, TournamentJoinForm
from GameRing_mod.models import Team, Tournament, User

# from rest_framework.decorators import api_view

#user
def login(request):
    return render(request, 'user/login.html')


def home(request):
    return render(request, 'user/home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            
            login(request)
            # login(request, user)

            return redirect('login')
    else:
        form = SignUpForm()

    return render(request, 'user/SignUp.html', {'form': form})

def create_player(request, team_id = -1, tournament_id = -1):

    user = User.authenticate_user(request)

#tournaments
def tournaments(request):
    context = {
        'tournaments': Tournament.objects.all()
    }
    return render(request, 'tournaments/tournaments.html')


def create_tournaments(request):
    form = TournamentCreationForm()
    if request.method == 'POST':
        form = TournamentCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('create')
    return render(request, 'tournaments/create_tournament.html', {'form': form})


def about_tournament(request, tournament_id):
    context = {
        'tournament_id': tournament_id,
        'tournament': Tournament.objects.get(id=tournament_id)
    }

    return render(request, 'tournaments/about_tournament.html', context)


def join_tournament(request, team_id, tournament_id):
    new_team = Team.objects.get(id=team_id)

    context = {
        'tournament_id': tournament_id,
        'tournament': Tournament.objects.get(id=tournament_id),
    }

    Tournament.teams.add(new_team)
    
    return render(request, 'tournaments/about_tournament.html', context)



class TournamentListView(ListView):
    model = Tournament
    template_name = 'tournaments/tournaments.html'
    context_object_name = 'tournaments'

#teams
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

#scrims
def scrims(request):
    return render(request, 'scrims/scrims.html')