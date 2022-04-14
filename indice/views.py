from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from .forms import Creacion
# Create your views here.


def inicio(request):
    return render(request, "index.html", {})


def iniciar_sesion(request):
    if request.method == "POST":
        form = Creacion(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(username=username, password=password)
            
            if user is not None:
                login(request, user)
                return render(request, "index.html", {"msj": "Iniciaste sesión!"})
            else:
                return render(request, "log2/iniciar_sesion.html", {"form": form, "msj": "No se autentico"})
        
        else:
            return render(request, "log2/iniciar_sesion.html", {"form": form, "msj": "Datos con formato incorrecto"})
    
    else:
        form = Creacion()
        return render(request, "log2/iniciar_sesion.html", {"form": form, "msj": ""})



def registrar(request):
    form = UserCreationForm()
    if request.method == "post":
        form = UserCreationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            form.save()
            return render(request, "index.html", {"msj": f"Se creo el user {username}"})
        else:
            return render(request, "log2/registrar.html", {"form": form, "msj": ""})
    return render(request, "log2/registrar.html", {"form": form, "msj": ""})