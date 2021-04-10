from django.urls import path
from . import views

urlpatterns = [
    path('', views.tournaments, name='tournaments'),
    path('create-tournament/', views.create_tournaments, name="create-tournament")

]