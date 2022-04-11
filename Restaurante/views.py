from django.shortcuts import render

from .models import Bebida, Comida, Empleado, Mesa

from .forms import ComidaFormulario, BebidaFormulario, MesaFormulario, EmpleadoFormulario
# Create your views here.

def formulario_comidas(request):
    formulario = ComidaFormulario()
    if request.method == "POST":
        formulario = ComidaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_comida = Comida(nombre=data["nombre"], clasificacion_en_carta=data["clasificacion_en_carta"], grande=data["grande"],
            chico=data["chico"])
            nueva_comida.save
        return render(request, "formulario_comidas.html", {"nueva_comida": nueva_comida, "formulario": formulario})
    return render(request, "formulario_comidas.html", {"formulario": formulario})


def formulario_bebidas(request):
    formulario = BebidaFormulario()
    if request.method == "POST":
        formulario = BebidaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_bebida = Bebida(nombre=data["nombre"], grande=data["grande"], chico=data["chico"])
            nueva_bebida.save
        return render(request, "formulario_bebidas.html", {"nueva_bebida": nueva_bebida, "formulario": formulario})
    return render(request, "formulario_bebidas.html", {"formulario": formulario})


def formulario_empleados(request):
    formulario = EmpleadoFormulario()
    if request.method == "POST":
        formulario = EmpleadoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_empleado = Empleado(nombre=data["nombre"], apellido=data["apellido"], mail=data["mail"], 
            puesto=data["puesto"])
            nuevo_empleado.save
        return render(request, "formulario_empleados.html", {"nuevo_empleado": nuevo_empleado, "formulario": formulario})
    return render(request, "formulario_empleados.html", {"formulario": formulario})


def formulario_mesas(request):
    formulario = MesaFormulario()
    if request.method == "POST":
        formulario = MesaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_mesa = Mesa(numero=data["numero"], grande=data["grande"], chica=data["chica"], 
            reservada=data["reservada"])
            nueva_mesa.save
        return render(request, "formulario_mesas.html", {"nueva_mesa": nueva_mesa, "formulario": formulario})
    return render(request, "formulario_mesas.html", {"formulario": formulario})

