# from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login_page, name='login_page'),
    path('logout/', views.logout_user, name='logout'),
    path('', views.home, name="home"),
    path('register', views.registration_page, name="register"),
]
