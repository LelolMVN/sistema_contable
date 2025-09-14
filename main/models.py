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

class Boletas(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    numero = models.CharField(max_length=36, unique=True, default=uuid.uuid4)  # N° boleta
    fecha_emision = models.DateTimeField(auto_now_add=True) # USE_TZ = True guarda en UTC
    cliente = models.CharField(max_length=200, null=True, blank=True) # Blank permite que el campo sea opcional
    total = models.DecimalField(max_digits=10, decimal_places=2)
    detalle = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return f"Boleta {self.numero} - {self.total}"