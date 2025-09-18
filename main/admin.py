from django.contrib import admin
from .models import Boletas, Bodegas, UnidadesMedida, Productos, Inventario

# Register your models here.
admin.site.register(Boletas)
admin.site.register(Bodegas)
admin.site.register(UnidadesMedida)
admin.site.register(Productos)
admin.site.register(Inventario)