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
    grande = models.BooleanField()
    chico = models.BooleanField()


class Bebida(models.Model):
    nombre = models.CharField(max_length=30)
    grande = models.BooleanField()
    chico = models.BooleanField()


class Mesa(models.Model):
    numero = models.IntegerField()
    grande = models.BooleanField()
    chica = models.BooleanField()
    reservada = models.BooleanField()