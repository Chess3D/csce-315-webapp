from django.urls import path
from . import views

urlpatterns = [
    path('', views.tournamentsHome, name='tournaments-home')
]