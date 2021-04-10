from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrims, name='scrims'),
]