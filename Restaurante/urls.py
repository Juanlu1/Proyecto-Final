from django.urls import path
from .views import formulario_comidas, formulario_bebidas, formulario_mesas, formulario_empleados

urlpatterns = [
    path("comidas/", formulario_comidas, name= "formulario_comidas"),
    path("bebidas/", formulario_bebidas, name= "formulario_bebidas"),
    path("mesas/", formulario_mesas, name= "formulario_mesas"),
    path("empleados/", formulario_empleados, name= "formulario_empleados"),
]
