from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate

from .models import UserInfo


from .forms import Creacion, Edicion, Login
# Create your views here.


def inicio(request):
    user_extension_logued, _ = UserInfo.objects.get_or_create(user=request.user)
    return render(request, "index.html", {"user_extension_logued": user_extension_logued})


def iniciar_sesion(request):
    if request.method == "POST":    
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]


            user = authenticate(username=username, password=password)
            
            if user is not None:
                
                login(request, user)
                user_extension_logued, _ = UserInfo.objects.get_or_create(user=request.user)
                return render(request, "index.html", {"msj": "Iniciaste sesión!", "user_extension_logued": user_extension_logued})
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
            user_extension_logued, _ = UserInfo.objects.get_or_create(user=request.user)
            return render(request, "index.html", {"msj": f"Se creo el user {username}", "user_extension_logued": user_extension_logued})
        else:
            return render(request, "log2/registrar.html", {"form": form, "msj": ""})
    
    return render(request, "log2/registrar.html", {"form": form, "msj": ""})




@login_required
def editar_user (request):
    msj = ""
    user_extension_logued, _ = UserInfo.objects.get_or_create(user=request.user)
    if request.method == "POST":
        form = Edicion(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            logued_user = request.user
            logued_user.username = data["username"]
            logued_user.email = data["email"]
            logued_user.first_name = data["first_name"]
            logued_user.last_name = data["last_name"]
            user_extension_logued.avatar = data["avatar"]
            user_extension_logued.link = data["link"]
            user_extension_logued.more_description = data["more_description"]
            
            if data.get("password1") == data.get("password2") and len(data.get("password1")) > 8:
                logued_user.set_password(data.get("password1"))
            else:
                msj = "No se modifico la contraseña."

            logued_user.save()
            user_extension_logued.save()
            print(data)
            return render (request, "index.html", {"msj": msj, "user_extension_logued": user_extension_logued})
        else:
            return render (request, "log2/editar_user.html", {"form": form, "msj": "", "user_extension_logued": user_extension_logued})
    
    form = Edicion(
        initial={
            "first_name": request.user.first_name,
            "last_name": request.user.last_name,
            "email": request.user.email,
            "username": request.user.username,
            "avatar": user_extension_logued.avatar,
            "link": user_extension_logued.link,
            "more_description": user_extension_logued.more_description,
        }
    )
    return render(request, "log2/editar_user.html", {"form": form, "msj": "", "user_extension_logued": user_extension_logued})



def about_me(request):
    user_extension_logued, _ = UserInfo.objects.get_or_create(user=request.user)
    return render(request, "about.html", {"user_extension_logued": user_extension_logued})


@login_required
def info_user(request):
    user_extension_logued, _ = UserInfo.objects.get_or_create(user=request.user)

    return render(request, "log2/info_user.html", {"logued_user": request.user, "user_extension_logued": user_extension_logued})


def accounts(request):
    user_extension_logued, _ = UserInfo.objects.get_or_create(user=request.user)
    return render(request, "log2/accounts.html", {"user_extension_logued": user_extension_logued})



