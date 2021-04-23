from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.urls import include, path
from GameRing_mod import views
from GameRing import settings

urlpatterns = [
     path('', views.scrims, name='scrims'),
]

if settings.DEBUG:
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
