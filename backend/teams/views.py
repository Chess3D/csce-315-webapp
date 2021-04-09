from django.shortcuts import render
from django.http import HttpResponse

def teamsHome(request):
    return HttpResponse('<h1>Teams</h1>')
