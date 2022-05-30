from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class Login(AuthenticationForm):
    username = forms.CharField(label= "Nombre de usuario")
    password = forms.CharField(label= "Contraseña", widget= forms.PasswordInput())

class Creacion(UserCreationForm):

    username = forms.CharField(label= "Nombre de usuario")
    email = forms.EmailField()
    password1 = forms.CharField(label= "Contraseña", widget= forms.PasswordInput())
    password2 = forms.CharField(label= "Repetir contraseña", widget= forms.PasswordInput())

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        help_texts = { k: "" for k in fields }



class Edicion(forms.Form):
    username = forms.CharField(label= "Nombre de usuario", required=False)
    email = forms.EmailField(required=False)
    password1 = forms.CharField(label= "Contraseña", widget= forms.PasswordInput(), required=False)
    password2 = forms.CharField(label= "Repetir contraseña", widget= forms.PasswordInput(), required=False)
    first_name = forms.CharField(label= "Nombre", max_length=20, required=False)
    last_name = forms.CharField(label= "Apellido", max_length=30, required=False)
    avatar = forms.ImageField(required=False)
    link = forms.CharField(label= "link", required=False, max_length=300)
    more_description = forms.CharField(label= "Descripción", required=False, max_length= 500)