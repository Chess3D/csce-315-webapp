from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginHome, name='login-home')
]