
from django import forms

class ComidaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    clasificacion_en_carta = forms.CharField(max_length=50)
    grande = forms.BooleanField()
    chico = forms.BooleanField()


class BebidaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    grande = forms.BooleanField()
    chico = forms.BooleanField()


class MesaFormulario(forms.Form):
    numero = forms.IntegerField()
    grande = forms.BooleanField()
    chica = forms.BooleanField()
    reservada = forms.BooleanField()


class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    mail = forms.EmailField()
    puesto = forms.CharField(max_length=20)