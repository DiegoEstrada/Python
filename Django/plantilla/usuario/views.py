from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from usuario.forms import RegistroForm
#from album.models import Category,Photo
#from django.views.generic import ListView, DetailView
#from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from django.urls import reverse_lazy 


# Create your views here.

def base(request):
    return render(request, 'adminlte/index.html')

def login(request):
    return render(request, 'adminlte/login.html')


class RegistoUsuario(CreateView):
    model = User
    template_name = "adminlte/registro.html"
    form_class = RegistroForm
    success_url = reverse_lazy('login')
    