from django.urls import path
from Restaurante import views

urlpatterns = [
    path("formulario/comidas/", views.formulario_comidas, name= "formulario_comidas"),
    path("formulario/bebidas/", views.formulario_bebidas, name= "formulario_bebidas"),
    path("formulario/mesas/", views.formulario_mesas, name= "formulario_mesas"),
    path("formulario/empleados/", views.formulario_empleados, name= "formulario_empleados"),

    path("bebidas/", views.listado_bebidas, name= "listado_bebidas"),
    path("comidas/", views.listado_comidas, name= "listado_comidas"),
    path("mesas/", views.listado_mesas, name= "listado_mesas"),
    path("empleados/", views.listado_empleados, name= "listado_empleados"),

    path("bebidas/borrar/<int:id>/", views.borrar_bebida, name= "borrar_bebida"),
    path("comida/borrar/<int:id>/", views.borrar_comida, name= "borrar_comida"),
    path("empleado/borrar/<int:id>/", views.borrar_empleado, name= "borrar_empleado"),
    path("mesa/borrar/<int:id>/", views.borrar_mesa, name= "borrar_mesa"),

    path("empleado/actualizar/<int:id>/", views.actualizar_empleado, name= "actualizar_empleado")
]
