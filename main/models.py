import uuid # para el nro de la boleta temporal
from django.db import models
from django.contrib.auth.models import User
'''
python manage.py makemigrations main - guardar cambios
python manage.py migrate - aplicar los cambios a la base de datos

python manage.py shell - acceder a la base de datos
from main.models import Columna1, Columna2
 

x = Tabla(columna="objeto")
x.save() - guardar
'''

class Boletas(models.Model): # Renonmbrar a ventas
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=36, unique=True, default=uuid.uuid4)  # N° boleta
    fecha_emision = models.DateTimeField(auto_now_add=True) # USE_TZ = True guarda en UTC
    cliente = models.CharField(max_length=200, null=True, blank=True) # Blank permite que el campo sea opcional
    total = models.DecimalField(max_digits=10, decimal_places=2)
    detalle = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"Boleta {self.numero} - {self.total}"
    
class Bodegas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50, unique=True)
    # sede/lugar fk

    def __str__(self):
        return f"{self.nombre}"

class UnidadesMedida(models.Model):
    nombre = models.CharField(max_length=50)
    simbolo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return f"{self.simbolo}"
    
class Productos(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    codigo = models.CharField(max_length=13, unique=True) # EAN-13
    nombre = models.CharField(max_length=100)
    unidad_medida = models.ForeignKey(UnidadesMedida, on_delete=models.PROTECT)
    precio = models.DecimalField(max_digits=8, decimal_places=2) # max 99,999,999

    def __str__(self):
        return f"{self.codigo}, {self.nombre}"

class Inventario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Usuario")
    bodega = models.ForeignKey(Bodegas, on_delete=models.CASCADE, verbose_name="Bodega")
    producto = models.ForeignKey(Productos, on_delete=models.CASCADE, verbose_name="Producto")
    cantidad = models.PositiveIntegerField(default=0, verbose_name="Cantidad en stock")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["bodega", "producto"], name="un_producto_por_bodega"),
        ]
    
    def aumentar_sotck(self, cantidad):
        self.cantidad += cantidad
        self.save()

    def disminuir_stock(self, cantidad):
        if cantidad <= self.cantidad:   
            self.cantidad -= cantidad
            self.save()
            return True
        return False
    
    def cantidad_stock(self):
        return self.cantidad

    def __str__(self):
        return f"Producto {self.producto} en {self.bodega}"
    
class Ventas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=36, unique=True, default=uuid.uuid4)  # N° boleta
    fecha_emision = models.DateTimeField(auto_now_add=True) # USE_TZ = True guarda en UTC
    producto = models.ForeignKey(Productos, on_delete=models.PROTECT)
    cantidad = models.PositiveIntegerField(default=0, verbose_name="Cantidad vendida")
    cliente = models.CharField(max_length=200, null=True, blank=True) # Blank permite que el campo sea opcional
    total = models.DecimalField(max_digits=10, decimal_places=2)
    detalle = models.CharField(max_length=300, null=True, blank=True)

    # El total debe ser el precio * cantidad vendida
    
    def __str__(self):
        return f"Boleta {self.numero} - {self.total}"