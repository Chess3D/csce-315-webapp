from django.shortcuts import render
from rest_framework import viewsets
from .serializers import WebappSerializer
from .models import Webapp

# Create your views here.
class WebappView(viewsets.ModelViewSet):
    serializer_class = WebappSerializer
    queryset = Webapp.objects.all()