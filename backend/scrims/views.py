from django.shortcuts import render
from django.http import HttpResponse

def scrimsHome(request):
    return HttpResponse('<h1>Scrimmages</h1>')
