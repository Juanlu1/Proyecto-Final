from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import Creacion, Edicion, Login
# Create your views here.


def inicio(request):
    return render(request, "index.html", {})


def iniciar_sesion(request):
    if request.method == "POST":    
        form = AuthenticationForm(request, data=request.POST)

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
        form = Login()
        return render(request, "log2/iniciar_sesion.html", {"form": form, "msj": ""})



def registrar(request):
    form = Creacion()

    if request.method == "POST":
        form = Creacion(request.POST)

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
    if request.method == "POST":
        form = Edicion(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            logued_user = request.user
            logued_user.username = data.get("username")
            logued_user.email = data.get("email")
            logued_user.first_name = data.get("first_name")
            logued_user.last_name = data.get("last_name")
            
            if data.get("password1") == data.get("password2") and len(data.get("password1")) > 8:
                logued_user.set_password(data.get("password1"))
            else:
                msj = "No se modifico la contraseña."

            logued_user.save()

            return render (request, "index.html", {"msj": msj})
        else:
            return render (request, "log2/editar_user.html", {"form": form, "msj": ""})
    
    form = Edicion(
        initial={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "username": request.user.username,
        }
    )
    return render(request, "log2/editar_user.html", {"form": form, "msj": ""})