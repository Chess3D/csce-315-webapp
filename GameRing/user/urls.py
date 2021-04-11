from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    path('', views.home, name='home'),

]