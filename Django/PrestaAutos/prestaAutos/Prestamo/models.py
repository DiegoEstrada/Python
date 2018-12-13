from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
from django.contrib.auth.models import User
from Automovil.models import Automovil

# Create your models here.

class TipoPrestamo(models.Model):
    nombre = models.CharField(max_length=30)
    dias = models.IntegerField()

    def __str__(self):
        return self.nombre




class Prestamo(models.Model):
    auto = models.ForeignKey(Automovil, on_delete=models.PROTECT)
    cliente = models.ForeignKey(User , on_delete=models.PROTECT)
    fecha_inicio = models.DateField(auto_now=True)
    fecha_fin = models.DateField(auto_now=False)
    observciones = models.TextField(blank=True)
    
    

    def __str__(self):
        return self.fecha_fin

