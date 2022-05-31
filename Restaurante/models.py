from django.db import models
from ckeditor.fields import RichTextField
from django.utils import timezone
# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    puesto = models.CharField(max_length=20)


class Comida(models.Model):
    nombre = models.CharField(max_length=30)
    clasificacion_en_carta = models.CharField(max_length=50)
    grande = models.BooleanField(null=True)
    chico = models.BooleanField(null=True)
    description = RichTextField(null=True, blank=True)
    imagen = models.ImageField(upload_to="avatares", null=True, blank=True, default= "")
    fecha_creacion = models.DateTimeField(default=timezone.now())



class Bebida(models.Model):
    nombre = models.CharField(max_length=30)
    grande = models.BooleanField(null=True)
    chico = models.BooleanField(null=True)
    description = RichTextField(null=True, blank=True)


class Mesa(models.Model):
    numero = models.IntegerField()
    grande = models.BooleanField(null=True)
    chica = models.BooleanField(null=True)
    reservada = models.BooleanField(null=True)