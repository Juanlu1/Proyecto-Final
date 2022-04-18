from django.db import models

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


class Bebida(models.Model):
    nombre = models.CharField(max_length=30)
    grande = models.BooleanField(null=True)
    chico = models.BooleanField(null=True)


class Mesa(models.Model):
    numero = models.IntegerField()
    grande = models.BooleanField(null=True)
    chica = models.BooleanField(null=True)
    reservada = models.BooleanField(null=True)