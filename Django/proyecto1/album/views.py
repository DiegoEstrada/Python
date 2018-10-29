from django.shortcuts import render
from django.http import HttpResponse
from album.models import Category,Photo
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, CreateView, DeleteView 
from django.urls import reverse_lazy 

# Create your views here.


def base(request):
    return render(request, 'base.html')

def first_view(request):
    return HttpResponse("Esta es mi primeara vista");

def category(request):
    category_list = Category.objects.all()
    context = {'object_list':category_list}
    return render(request,'category.html',context)

def category_detail(request, id_category):
    category = Category.objects.get(id=id_category)
    context = {'object':category}
    return render(request,'category_detail.html',context)

class PhotoListView(ListView):
    model = Photo

class PhotoDetailView(DetailView):
    model = Photo

class CategoryListView(ListView):
    model = Category

class CategoryDetailView(DetailView):
    model = Category

class PhotoUpdate(UpdateView):
    model = Photo
    fields = '__all__'

class PhotoCreate(CreateView):
    model = Photo
    fields = '__all__'

class PhotoDelete(DeleteView):
    model = Photo
    success_url = reverse_lazy('photo-list')