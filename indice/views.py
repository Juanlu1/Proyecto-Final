from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import Creacion, Edicion
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




@login_required
def editar_user (request):
    msj = ""
    request.user

    if request.method == "post":
        form = Edicion(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            logued_user = request.user

            logued_user.email = data.get("email", "")
            logued_user.first_name = data.get("first_name", "")
            logued_user.last_name = data.get("last_name", "")
            
            if data.get("password1") == data.get("password2") and len(data.get("password1")) > 8:
                logued_user.set_password(data.get("password1"))
            else:
                msj = "No se modifico la contraseña."

            logued_user.save()

            return render (request, "index.html", {"msj": msj})
        else:
            return render (request, "log2/editar_user.html", {"form": form, "msj": msj})
