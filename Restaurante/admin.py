from django.contrib import admin

from Restaurante.models import Bebida, Comida, Empleado, Mesa

# Register your models here.

admin.site.register(Empleado)
admin.site.register(Comida)
admin.site.register(Bebida)
admin.site.register(Mesa)