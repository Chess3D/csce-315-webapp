from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include, path
from GameRing_mod import views
from GameRing import settings

urlpatterns = [
    #Teams
    path('', views.TeamListView.as_view(), name='teams'),
    path('create/', views.create, name="create"),
    path('join/<team_id>', views.join_team, name="join_team"),
    path('<team_id>/', views.about_team, name='about_team'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
