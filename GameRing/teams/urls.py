from django.urls import path
from . import views

urlpatterns = [
    path('', views.teams, name='teams'),
    path('create/', views.create, name="create"),
]