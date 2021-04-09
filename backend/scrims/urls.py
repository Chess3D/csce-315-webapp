from django.urls import path
from . import views

urlpatterns = [
    path('', views.scrimsHome, name='scrims-home')
]