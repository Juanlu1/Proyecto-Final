from django.urls import path
from Restaurante import views

urlpatterns = [
    path("formulario/comidas/", views.formulario_comidas, name= "formulario_comidas"),
    path("formulario/bebidas/", views.formulario_bebidas, name= "formulario_bebidas"),
    path("formulario/mesas/", views.formulario_mesas, name= "formulario_mesas"),
    path("formulario/empleados/", views.formulario_empleados, name= "formulario_empleados"),

    path("pages/bebidas/", views.listado_bebidas, name= "listado_bebidas"),
    path("pages/comidas/", views.listado_comidas, name= "listado_comidas"),
    path("pages/mesas/", views.listado_mesas, name= "listado_mesas"),
    path("pages/empleados/", views.listado_empleados, name= "listado_empleados"),

    path("pages/bebidas/borrar/<int:id>/", views.borrar_bebida, name= "borrar_bebida"),
    path("pages/comida/borrar/<int:id>/", views.borrar_comida, name= "borrar_comida"),
    path("pages/empleado/borrar/<int:id>/", views.borrar_empleado, name= "borrar_empleado"),
    path("pages/mesa/borrar/<int:id>/", views.borrar_mesa, name= "borrar_mesa"),

    path("pages/empleado/actualizar/<int:id>", views.actualizar_empleado, name= "actualizar_empleado"),
    path("pages/bebidas/actualizar/<int:id>", views.actualizar_bebida, name= "actualizar_bebida"),
    path("pages/comida/actualizar/<int:id>", views.actualizar_comida, name= "actualizar_comida"),
    path("pages/mesa/actualizar/<int:id>", views.actualizar_mesa, name= "actualizar_mesa"),

    path("pages/empleado/info/<int:id>", views.info_empleados, name= "info_empleados"),
    path("pages/bebidas/info/<int:id>", views.info_bebidas, name= "info_bebidas"),
    path("pages/comida/info/<int:id>", views.info_comidas, name= "info_comidas"),
    path("pages/mesa/info/<int:id>", views.info_mesas, name= "info_mesas"),
]
