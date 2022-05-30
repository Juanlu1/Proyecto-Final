from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

from .models import Bebida, Comida, Empleado, Mesa
from .forms import ComidaFormulario, BebidaFormulario, MesaFormulario, EmpleadoFormulario
# Create your views here.


@login_required
def formulario_comidas(request):
    formulario = ComidaFormulario()

    if request.method == "POST":
        formulario = ComidaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_comida = Comida(nombre=data["nombre"], clasificacion_en_carta=data["clasificacion_en_carta"], grande=data["grande"],
            chico=data["chico"])
            nueva_comida.save()
        listado_comidas = Comida.objects.all()
        return render(request, "index.html", {"listado_comidas": listado_comidas})
    return render(request, "restaurante/formulario_comidas.html", {"formulario": formulario})

@login_required
def formulario_bebidas(request):
    formulario = BebidaFormulario()
    if request.method == "POST":
        formulario = BebidaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_bebida = Bebida(nombre=data["nombre"], grande=data["grande"], chico=data["chico"])
            nueva_bebida.save()
        return render(request, "index.html", {})
    return render(request, "restaurante/formulario_bebidas.html", {"formulario": formulario})

@login_required
def formulario_empleados(request):
    formulario = EmpleadoFormulario()
    if request.method == "POST":
        formulario = EmpleadoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_empleado = Empleado(nombre=data["nombre"], apellido=data["apellido"], mail=data["mail"], 
            puesto=data["puesto"])
            nuevo_empleado.save()
        return render(request, "index.html", {})
    return render(request, "restaurante/formulario_empleados.html", {"formulario": formulario})

@login_required
def formulario_mesas(request):
    formulario = MesaFormulario()
    if request.method == "POST":
        formulario = MesaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_mesa = Mesa(numero=data["numero"], grande=data["grande"], chica=data["chica"], 
            reservada=data["reservada"])
            nueva_mesa.save()
        return render(request, "index.html", {})
    return render(request, "restaurante/formulario_mesas.html", {"formulario": formulario})






def listado_comidas(request):
    listado_comidas = Comida.objects.all()
    return render(request, "listados/listado_comidas.html", {"listado_comidas": sorted(listado_comidas, key=lambda x: x.nombre)})


def listado_mesas(request):
    listado_mesas = Mesa.objects.all()
    return render(request, "listados/listado_mesas.html", {"listado_mesas": sorted(listado_mesas, key=lambda x: x.numero)})


def listado_empleados(request):
    listado_empleados = Empleado.objects.all()
    return render(request, "listados/listado_empleados.html", {"listado_empleados": sorted(listado_empleados, key=lambda x: x.nombre)})


def listado_bebidas(request):
    listado_bebidas = Bebida.objects.all()
    return render(request, "listados/listado_bebidas.html", {"listado_bebidas": sorted(listado_bebidas, key=lambda x: x.nombre)})





@login_required
def borrar_comida(request, id):
    comida = Comida.objects.get(id=id)
    comida.delete()
    return redirect("listado_comidas")

@login_required
def borrar_bebida(request, id):
    bebida = Bebida.objects.get(id=id)
    bebida.delete()
    return redirect("listado_bebidas")

@login_required
def borrar_mesa(request, id):
    mesa = Mesa.objects.get(id=id)
    mesa.delete()
    return redirect("listado_mesas")

@login_required
def borrar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect("listado_empleados")



@login_required
def actualizar_empleado(request, id):

    empleado = Empleado.objects.get(id=id)

    if request.method == "POST":
        formulario = EmpleadoFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            empleado.nombre = data["nombre"]
            empleado.apellido = data["apellido"]
            empleado.mail = data["mail"]
            empleado.puesto = data["puesto"]
            empleado.save()
        return redirect("listado_empleados")
    
    formulario = EmpleadoFormulario(
        initial={
            "nombre": empleado.nombre,
            "apellido": empleado.apellido,
            "mail": empleado.mail,
            "puesto": empleado.puesto
        }
    )

    return render(request, "actualizar/empleados.html", {"formulario": formulario, "empleado": empleado})



@login_required
def actualizar_comida(request, id):

    comida = Comida.objects.get(id=id)

    if request.method == "POST":
        formulario = ComidaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            comida.nombre = data["nombre"]
            comida.clasificacion_en_carta = data["clasificacion_en_carta"]
            comida.grande = data["grande"]
            comida.chico = data["chico"]
            comida.save()
        return redirect("listado_comidas")
    
    formulario = ComidaFormulario(
        initial={
            "nombre": comida.nombre,
            "clasificacion_en_carta": comida.clasificacion_en_carta,
            "grande": comida.grande,
            "chico": comida.chico
        }
    )

    return render(request, "actualizar/comidas.html", {"formulario": formulario, "comida": comida})




@login_required
def actualizar_bebida(request, id):

    bebida = Bebida.objects.get(id=id)

    if request.method == "POST":
        formulario = BebidaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            bebida.nombre = data["nombre"]
            bebida.grande = data["grande"]
            bebida.chico = data["chico"]
            bebida.save()
        return redirect("listado_bebidas")
    
    formulario = BebidaFormulario(
        initial={
            "nombre": bebida.nombre,
            "grande": bebida.grande,
            "chico": bebida.chico
        }
    )

    return render(request, "actualizar/bebidas.html", {"formulario": formulario, "bebida": bebida})




@login_required
def actualizar_mesa(request, id):

    mesa = Mesa.objects.get(id=id)

    if request.method == "POST":
        formulario = MesaFormulario(request.POST)

        if formulario.is_valid():
            data = formulario.cleaned_data
            mesa.numero = data["numero"]
            mesa.grande = data["grande"]
            mesa.chica = data["chica"]
            mesa.reservada = data["reservada"]
            mesa.save()
        return redirect("listado_mesas")
    
    formulario = MesaFormulario(
        initial={
            "numero": mesa.numero,
            "reservada": mesa.reservada,
            "grande": mesa.grande,
            "chica": mesa.chica
        }
    )

    return render(request, "actualizar/mesas.html", {"formulario": formulario, "mesa": mesa})







@login_required
def info_comidas(request, id):
    comida = Comida.objects.get(id=id)
    return render(request, "Info/info_comidas.html", {"comida": comida})
    


@login_required
def info_bebidas(request, id):
    bebida = Bebida.objects.get(id=id)
    return render(request, "Info/info_bebidas.html", {"bebida": bebida})



@login_required
def info_empleados(request, id):
    empleado = Empleado.objects.get(id=id)
    return render(request, "Info/info_empleados.html", {"empleado": empleado})



@login_required
def info_mesas(request, id):
    mesa = Mesa.objects.get(id=id)
    return render(request, "Info/info_mesas.html", {"mesa": mesa})
    