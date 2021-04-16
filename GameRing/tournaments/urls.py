from django.urls import path
from . import views
from .views import TournamentListView

urlpatterns = [
    path('', TournamentListView.as_view(), name='tournaments'),
    path('create/', views.create_tournaments, name="create-tournament")
]