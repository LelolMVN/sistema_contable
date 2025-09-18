from django import forms
from django.forms import ModelForm
from .models import Boletas, UnidadesMedida, Bodegas, Productos, Inventario

# required = true por default

# ASEGURARSE QUE LOS FORM SOLO MUESTREN DATOS DEL USUARIO Y NO DE LOS DEMÁS
# por ahora no lo cumple

class CrearBoleta(ModelForm):
    class Meta:
        model = Boletas
        fields = ["cliente", "total", "detalle"]

class IngresarProducto(ModelForm):
    class Meta:
        model = Productos
        fields = ["codigo", "nombre", "unidad_medida", "precio"]

class AgregarAlInventario(ModelForm):
    class Meta:
        model = Inventario
        fields = ["bodega", "producto", "cantidad"]
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop("user")
        super().__init__(*args, **kwargs)

        self.fields["bodega"].queryset = Bodegas.objects.filter(user=user)
        self.fields["producto"].queryset = Productos.objects.filter(user=user)