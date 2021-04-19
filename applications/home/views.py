from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, ListView
# import models
from .models import Prueba

class PruebaView(TemplateView):
    template_name = 'home/prueba.html'


class PruebaListView(ListView):
    template_name = 'home/lista.html'
    context_object_name = 'listaNumeros'
    queryset = ['0', '10', '20', '30'] 

class ListarPrueba(ListView):
    template_name = 'home/lista_prueba.html'
    model = Prueba
    context_object_name = 'lista'