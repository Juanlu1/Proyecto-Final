from django.shortcuts import render

from .models import Bebida, Comida, Empleado, Mesa

from .forms import (ComidaFormulario, BebidaFormulario, MesaFormulario, EmpleadoFormulario, BusquedaBebida, 
BusquedaComida, BusquedaEmpleado, BusquedaMesa)
# Create your views here.

def formulario_comidas(request):
    buscador = BusquedaComida()
    formulario = ComidaFormulario()

    if request.method == "POST":
        form = ComidaFormulario(request.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            nueva_comida = Comida(nombre=data["nombre"], clasificacion_en_carta=data["clasificacion_en_carta"], grande=data["grande"],
            chico=data["chico"])
            nueva_comida.save
        return render(request, "formulario_comidas.html", {"nueva_comida": nueva_comida, "buscador": buscador, "formulario": formulario})
    
    if request.method == "GET":
        Comidas_buscadas = []
        dato = request.GET.get("partial_comida", None)

        if dato is not None:
            Comidas_buscadas = Comida.objects.filter(nombre_icontains=dato)
            return (request, "formulario_comidas.html", {"nueva_comida": nueva_comida, "buscador": buscador, 
            "Comidas_buscadas": Comidas_buscadas, "formulario": formulario})
    return render(request, "formulario_comidas.html", {"formulario": formulario})


def formulario_bebidas(request):
    buscador = BusquedaBebida()
    formulario = BebidaFormulario()
    if request.method == "POST":
        formulario = BebidaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_bebida = Bebida(nombre=data["nombre"], grande=data["grande"], chico=data["chico"])
            nueva_bebida.save
        return render(request, "formulario_bebidas.html", {"nueva_bebida": nueva_bebida, "buscador": buscador, "formulario": formulario})
       
    if request.method == "GET":
        Bebidas_buscadas = []
        dato = request.GET.get("partial_bebida", None)

        if dato is not None:
            Bebidas_buscadas = Bebida.objects.filter(nombre_icontains=dato)
            return (request, "formulario_bebidas.html", {"nueva_bebida": nueva_bebida, "buscador": buscador, 
            "Bebidas_buscadas": Bebidas_buscadas, "formulario": formulario})
    return render(request, "formulario_bebidas.html", {"formulario": formulario})


def formulario_empleados(request):
    buscador = BusquedaEmpleado()
    formulario = EmpleadoFormulario()
    if request.method == "POST":
        formulario = EmpleadoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_empleado = Empleado(nombre=data["nombre"], apellido=data["apellido"], mail=data["mail"], 
            puesto=data["puesto"])
            nuevo_empleado.save
        return render(request, "formulario_empleados.html", {"nuevo_empleado": nuevo_empleado, "buscador": buscador, 
        "formulario": formulario})

    if request.method == "GET":
        Empleados_buscados = []
        dato = request.GET.get("partial_empleado", None)

        if dato is not None:
            Empleados_buscados = Empleado.objects.filter(nombre_icontains=dato)
            return (request, "formulario_empleados.html", {"nuevo_empleado": nuevo_empleado, "buscador": buscador, 
            "Empleados_buscados": Empleados_buscados, "formulario": formulario})
    return render(request, "formulario_empleados.html", {"formulario": formulario})


def formulario_mesas(request):
    buscador = BusquedaMesa()
    formulario = MesaFormulario()
    if request.method == "POST":
        formulario = MesaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_mesa = Mesa(numero=data["numero"], grande=data["grande"], chica=data["chica"], 
            reservada=data["reservada"])
            nueva_mesa.save
        return render(request, "formulario_mesas.html", {"nueva_mesa": nueva_mesa, "buscador": buscador, "formulario": formulario})

    if request.method == "GET":
        Mesas_buscadas = []
        dato = request.GET.get("partial_mesa", None)

        if dato is not None:
            Mesas_buscadas = Empleado.objects.filter(nombre_icontains=dato)
            return (request, "formulario_mesas.html", {"nueva_mesa": nueva_mesa, "buscador": buscador, 
            "Mesas_buscadas": Mesas_buscadas, "formulario": formulario})
    return render(request, "formulario_mesas.html", {"formulario": formulario})

