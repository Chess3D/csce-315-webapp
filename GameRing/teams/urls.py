from django.urls import path
from . import views
from .views import TeamListView

urlpatterns = [
    path('', TeamListView.as_view(), name='teams'),
    path('create/', views.create, name="create"),
    path('join/<team_id>', views.join_team, name="join_team"),
    path('<team_id>/', views.about_team, name='about_team'),
]