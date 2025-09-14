from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("ventas/", views.ventas, name="ventas"),
    path("boletas/", views.boletas, name="boletas")
]