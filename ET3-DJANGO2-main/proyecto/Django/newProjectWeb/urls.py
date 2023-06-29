
from django.contrib import admin
from django.urls import path, include 
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('form1', views.form1, name='form1'),
    path('plants', views.plants, name='plants'),
    path('suscripcion', views.suscripcion, name='suscripcion'),
    path('listProducto', views.listProducto, name='listProducto'),
    path('crud', views.crud, name='crud'),
    path('addProducto', views.addProducto, name='addProducto'),
    path('delProducto/<str:pk>', views.delProducto, name='delProducto'),
    path('retModProducto/<str:pk>', views.retModProducto, name ="retModProducto"),
    path('updProducto', views.updProducto, name="updProducto"),
    path('formAdd', views.formAdd, name = "formAdd"),
    path('userAdd'),
    path('userEdit',),
    path('userList', ),
    path("", views.login, name="login"),
    path("logout", views.logout, name="logout"),


]