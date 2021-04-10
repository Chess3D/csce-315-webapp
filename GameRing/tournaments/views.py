from django.shortcuts import render
from django.http import HttpResponse

def tournaments(request):
    return render(request, 'tournaments/tournaments.html')
