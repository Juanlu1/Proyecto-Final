from django.shortcuts import redirect, render

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
        return render(request, "restaurante/formulario_comidas.html", {})
    return render(request, "restaurante/formulario_comidas.html", {"formulario": formulario})


def formulario_bebidas(request):
    formulario = BebidaFormulario()
    if request.method == "POST":
        formulario = BebidaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_bebida = Bebida(nombre=data["nombre"], grande=data["grande"], chico=data["chico"])
            nueva_bebida.save
        return render(request, "restaurante/formulario_bebidas.html", {})
    return render(request, "restaurante/formulario_bebidas.html", {"formulario": formulario})


def formulario_empleados(request):
    formulario = EmpleadoFormulario()
    if request.method == "POST":
        formulario = EmpleadoFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nuevo_empleado = Empleado(nombre=data["nombre"], apellido=data["apellido"], mail=data["mail"], 
            puesto=data["puesto"])
            nuevo_empleado.save
        return render(request, "restaurante/formulario_empleados.html", {})
    return render(request, "restaurante/formulario_empleados.html", {"formulario": formulario})


def formulario_mesas(request):
    formulario = MesaFormulario()
    if request.method == "POST":
        formulario = MesaFormulario(request.POST)
        
        if formulario.is_valid():
            data = formulario.cleaned_data
            nueva_mesa = Mesa(numero=data["numero"], grande=data["grande"], chica=data["chica"], 
            reservada=data["reservada"])
            nueva_mesa.save
        return render(request, "restaurante/formulario_mesas.html", {})
    return render(request, "restaurante/formulario_mesas.html", {"formulario": formulario})






def listado_comidas(request):
    listado_comidas = Comida.objects.all()
    return render(request, "listados/listado_comidas.html", {"listado_comidas": listado_comidas})


def listado_mesas(request):
    listado_mesas = Mesa.objects.all()
    return render(request, "listados/listado_mesas.html", {"listado_mesas": listado_mesas})


def listado_empleados(request):
    listado_empleados = Empleado.objects.all()
    return render(request, "listados/listado_empleados.html", {"listado_empleados": listado_empleados})


def listado_bebidas(request):
    listado_bebidas = Bebida.objects.all()
    return render(request, "listados/listado_bebidas.html", {"listado_bebidas": listado_bebidas})






def borrar_comida(request, id):
    comida = Comida.objects.get(id=id)
    comida.delete()
    return redirect("listado_comidas")


def borrar_bebida(request, id):
    bebida = Bebida.objects.get(id=id)
    bebida.delete()
    return redirect("listado_bebidas")


def borrar_mesa(request, id):
    mesa = Mesa.objects.get(id=id)
    mesa.delete()
    return redirect("listado_mesas")


def borrar_empleado(request, id):
    empleado = Empleado.objects.get(id=id)
    empleado.delete()
    return redirect("listado_empleados")




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
            empleado.save
        return redirect("listado_empleados")
    
    formulario = EmpleadoFormulario(
        intial={
            "nombre": empleado.nombre,
            "apellido": empleado.apellido,
            "mail": empleado.mail,
            "puesto": empleado.puesto
        }
    )

    return render(request, "actualizar/empleados.html", {"formulario": formulario})