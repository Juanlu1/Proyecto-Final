
from django.utils import timezone
from django import forms
from ckeditor.fields import RichTextFormField

class ComidaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    clasificacion_en_carta = forms.CharField(max_length=50)
    grande = forms.BooleanField(required=False)
    chico = forms.BooleanField(required=False)
    description = RichTextFormField(required=False)
    imagen = forms.ImageField(required=False)


class BebidaFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    grande = forms.BooleanField(required=False)
    chico = forms.BooleanField(required=False)
    description = RichTextFormField(required=False)

class MesaFormulario(forms.Form):
    numero = forms.IntegerField()
    grande = forms.BooleanField(required=False)
    chica = forms.BooleanField(required=False)
    reservada = forms.BooleanField(required=False)


class EmpleadoFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    apellido = forms.CharField(max_length=30)
    mail = forms.EmailField()
    puesto = forms.CharField(max_length=20)