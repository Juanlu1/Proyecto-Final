from django.db import models

# Create your models here.

class Empleado(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    mail = models.EmailField()
    puesto = models.CharField(max_length=20)
    def __str__(self):
        return f"Nombre: {self.nombre} - Apellido: {self.apellido} - mail: {self.mail} - puesto: {self.puesto}"


class Comida(models.Model):
    nombre = models.CharField(max_length=30)
    clasificacion_en_carta = models.CharField(max_length=50)
    grande = models.BooleanField()
    chico = models.BooleanField()
    def __str__(self):
        return f"Nombre: {self.nombre} - Clasificacion en carta: {self.clasificacion_en_carta}"


class Bebida(models.Model):
    nombre = models.CharField(max_length=30)
    grande = models.BooleanField()
    chico = models.BooleanField()
    def __str__(self):
        return f"Nombre: {self.nombre}"


class Mesa(models.Model):
    numero = models.IntegerField()
    grande = models.BooleanField()
    chica = models.BooleanField()
    reservada = models.BooleanField()
    def __str__(self):
        return f"Numero: {self.numero}"