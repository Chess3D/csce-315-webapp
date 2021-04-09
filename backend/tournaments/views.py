from django.shortcuts import render
from django.http import HttpResponse

def tournamentsHome(request):
    return HttpResponse('<h1>Tournaments</h1>')
