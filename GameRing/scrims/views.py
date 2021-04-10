from django.shortcuts import render
from django.http import HttpResponse

def scrims(request):
    return render(request, 'scrims/scrims.html')
