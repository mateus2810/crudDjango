from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings


urlpatterns = [

    path('cliente/', views.cliente, name='cliente'),
    path('home/', views.home, name='home'),
    path('listarCliente/', views.listarCliente, name='listarCliente'),
    path('excluirCliente/<pk>', views.excluirCliente, name='excluirCliente'),
    path('editarCliente/<pk>', views.editarCliente, name='editarCliente')

]