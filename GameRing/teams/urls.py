from django.urls import path
from . import views
from .views import TeamListView

urlpatterns = [
    path('', TeamListView.as_view(), name='teams'),
    path('create/', views.create, name="create"),
    path('<team_id>/', views.about_team, name='about_team'),
]