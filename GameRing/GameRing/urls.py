from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    #GameRing
    path('', include('GameRing_mod.urls.user_urls')),
    path('admin/', admin.site.urls),
    path('user/', include('GameRing_mod.urls.user_urls')),
    path('scrims/', include('GameRing_mod.urls.scrim_urls')),
    path('tournaments/', include('GameRing_mod.urls.tournament_urls')),
    path('teams/', include('GameRing_mod.urls.team_urls')),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
