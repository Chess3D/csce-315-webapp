from django.urls import path, include
from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('login/', views.login, name='login'),
    url(r'^signup/$', views.signup, name='signup'),
    # path('signup/', views.signup, name= 'signup'),
    path('', views.home, name='home'),

]