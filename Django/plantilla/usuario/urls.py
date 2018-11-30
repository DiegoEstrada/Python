from django.urls import path
from usuario.views import RegistoUsuario
from django.contrib.auth import views as auth_view
from . import views

urlpatterns = [
    path('', views.base, name='base'),
    path('registrar/', RegistoUsuario.as_view(), name='registro'),
    path('login/', auth_view.LoginView.as_view(template_name='adminlte/login.html'), name='login'),
    path('logout/', auth_view.LoginView.as_view(template_name='adminlte/login.html'), name='logout'),
]