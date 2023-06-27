
from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('form1', views.form1, name='form1'),
    path('plants', views.plants, name='plants'),
    path('suscripcion', views.suscripcion, name='suscripcion'),

]