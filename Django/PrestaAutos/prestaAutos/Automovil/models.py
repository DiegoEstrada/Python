from django.db import models
from django.db.models.signals import post_delete
from django.dispatch import receiver
from django.urls import reverse
import datetime

# Create your models here.

class Marca(models.Model):
    compania = models.CharField(max_length=30)
    imagen = models.ImageField(upload_to="marcas/")
    pais = models.CharField(max_length=20)

    def __str__(self):
        return self.compania


class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Automovil(models.Model):
    matricula = models.CharField(max_length=8, primary_key=True)
    nombre = models.CharField(max_length=50)
    anio = models.CharField(max_length=4,default=str(datetime.datetime.now().year),editable=True)
    foto = models.ImageField(upload_to='autos/')
    capacidad = models.IntegerField()
    disponible = models.BooleanField(default=True)
    marca = models.ForeignKey(Marca, on_delete=models.PROTECT)
    tipo = models.ForeignKey(Categoria, on_delete=models.PROTECT)
    

    def __str__(self):
        return self.nombre


@receiver(post_delete, sender=Automovil)
def photo_delete(sender, instance, **kwargs):
    instance.foto.delete(True)