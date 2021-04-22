from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Tournament
from django.views.generic import ListView
from teams.models import Team
# from rest_framework.decorators import api_view

from .forms import TournamentCreationForm
from .forms import TournamentJoinForm


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


def about_team(request, tournament_id):
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

# @api_view(['GET', 'POST'])
# def tournaments_list(request):
#     if request.method == 'GET':
#         data = Tournament.objects.all()
#         serializer = TournamentSerializer(data, context={'request', request}, many=True)
#         return HttpResponse(serializer.data)
#     elif request.method == 'POST':
#         serializer = TournamentSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(status=status.HTTP_201_CREATED)


# @api_view(['PUT', 'DELETE'])
# def tournaments_details(request, pk):
#     try:
#         tournament = Tournament.objects.get(pk=pk)
#     except Tournament.DoesNotExist:
#         return HttpResponse(status=status.HTTP_404_NOT_FOUND)

#     if request.method == 'PUT':
#         serializer = TournamentSerializer(tournament, data=request.data, context={'request', request})
#         if serializer.is_valid():
#             serializer.save()
#             return HttpResponse(status=status.HTTP_400_BAD_REQUEST)

#     elif request.method == 'DELETE':
#         student.delete()
#         return HttpResponse(status=status.HTTP_204_NO_CONTENT)



