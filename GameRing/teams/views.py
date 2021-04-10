from django.shortcuts import render
from django.http import HttpResponse

def teams(request):
    return render(request, 'teams/teams.html')
