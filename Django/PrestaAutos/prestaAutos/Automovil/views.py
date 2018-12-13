from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from django.urls import reverse_lazy 
from Automovil.models import Automovil,Categoria,Marca

# Create your views here.
def base(request):
    return render(request, 'adminlte/index.html')
    
def bas(request):
    return render(request, 'adminlte/login.html')

class AutomovilListView(ListView):
    model = Automovil

class CategoriaListView(ListView):
    model = Categoria

class MarcaListView(ListView):
    model = Marca

