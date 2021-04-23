from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include, path
from GameRing_mod import views
from GameRing import settings

urlpatterns = [
    #Tournaments
    path('', views.TournamentListView.as_view(), name='tournaments'),
    path('create/', views.create_tournaments, name="create-tournament"),
    path('<tournament_id>/', views.about_team, name='about_tournament'),
    path('<tournament_id>/join/<team_id>/', views.join_tournament, name='join-tournament'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
