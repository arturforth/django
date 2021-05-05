from django.contrib import admin
from django.urls import path
from . import views     # importo desde el directorio en el que esta urls.py

urlpatterns = [
    path('listar-todo-empleados/', views.ListAllEmpleados.as_view()),
]