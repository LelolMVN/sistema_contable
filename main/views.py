from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Boletas, Productos, Inventario, Bodegas
from .forms import CrearBoleta, IngresarProducto, AgregarAlInventario
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

def index(request):
    return render(request, 'main/index.html', {})

@login_required
def ventas(request):
    boletas = Boletas.objects.all()

    if request.method == "POST":
        form = CrearBoleta(request.POST)

        if form.is_valid():
            cliente = form.cleaned_data["cliente"]
            total = form.cleaned_data["total"]
            detalle = form.cleaned_data["detalle"]

            boleta = Boletas(user=request.user, cliente=cliente, total=total, detalle=detalle)
            boleta.save()

            return HttpResponseRedirect(reverse('ventas'))
        
    else:
        form = CrearBoleta()

    return render(request, "main/ventas.html", {"form":form, "boletas":boletas})

@login_required
def boletas(request):
    boletas = Boletas.objects.all()

    return render(request, "main/boletas.html", {"boletas":boletas})

@login_required
def perfil(request):
    
    usuario_dict = {
        "usuario":request.user.username,
        "email": request.user.email,
    }

    return render(request, "main/perfil.html", usuario_dict)

@login_required
def inventario(request):
    inventario = Inventario.objects.all()

    user = request.user

    if not user.bodegas_set.exists():
        # Crear una bodega por si no tiene
        bodega = Bodegas(user=user, nombre=f"Bodega {user.username}")
        bodega.save()

    if request.method == "POST":
        form = AgregarAlInventario(request.POST, user=user)

        if form.is_valid():
            agregar_al_inventario = form.save(commit=False) # Crear pero no guardar aun
            agregar_al_inventario.user = user
            agregar_al_inventario.save()

            return HttpResponseRedirect(reverse('inventario'))
        
    else:
        form = AgregarAlInventario(user=user)

    return render(request, "main/inventario.html", {"form":form, "inventario":inventario})

@login_required
def productos(request):
    productos = Productos.objects.all()

    user = request.user

    if request.method == "POST":
        form = IngresarProducto(request.POST)

        if form.is_valid():
            ingresar_producto = form.save(commit=False)
            ingresar_producto.user = user
            ingresar_producto.save()

            return HttpResponseRedirect(reverse('productos'))
    else:
        form = IngresarProducto()

    return render(request, "main/productos.html", {"form": form, "productos": productos})

'''
def index(request, nombre):
    producto = Productos.objects.get(nombre=nombre)
    venta = Ventas.objects.get(id=1)

    dict = {
    "producto": producto.nombre
    }
    return render(request, 'main/index.html', dict)
'''