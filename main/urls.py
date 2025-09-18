from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ventas/", views.ventas, name="ventas"),
    path("boletas/", views.boletas, name="boletas"),
    path("perfil/", views.perfil, name="perfil"),
    path("inventario/", views.inventario, name="inventario"),
    path("productos/", views.productos, name="productos"),
]