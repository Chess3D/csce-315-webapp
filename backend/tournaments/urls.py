from django.urls import path
from . import views

urlpatterns = [
    path('admin/', views.tournaments, name='tournaments')
    re_path(r'^ttps://api.challonge.com/v1/tournaments.{json|xml}', views.tournaments_list)
    re_path(r'^https://api.challonge.com/v1/tournaments/{tournament}.{json|xml}', views.tournaments_details)
]