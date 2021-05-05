from django.shortcuts import render
from django.views.generic import ListView
# models
from .models import Empleado

class ListAllEmpleados(ListView):
    template_name = 'persona/list_all.html'
    model = Empleado
    # Sin usar context_object_name, se puede acceder a la lista con el nombre 'object_list'. Ver documentacion de ListView!
    context_object_name = 'lista'   # Nombre para acceder a la lista desde el archivo html


# Objetivos:
# 1) Listar todos los empleados de la empresa
# 2) Listar todos los empleados que pertenecen a un area de la empresa
# 3) Listar empleados por trabajo
# 4) Listar habilidades de un empleado

