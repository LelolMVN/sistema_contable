from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Boletas, Productos, Inventario, Bodegas, Ventas
from .forms import CrearBoleta, IngresarProducto, AgregarAlInventario, AgregarVenta
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.models import User

def index(request):
    return render(request, 'main/index.html', {})

@login_required
def ventas(request):
    ventas = Ventas.objects.all()
    user = request.user

    if request.method == "POST":
        form = AgregarVenta(request.POST, user=user)

        # HACER:
        '''
        1. Poder solo crear ventas de lo que hay en el inventario.
        Por ahora sew puede de cualquier producto y cualquier cantidad
        2. Validar si hay stock que se pueda vender. Sino dar un aviso.
        3. Eliminar la cantidad vendida del inventario buscando por id del producto.
        '''
       
        if form.is_valid():
            nueva_venta = form.save(commit=False)
            nueva_venta.user = user

            nueva_venta.save()

            return HttpResponseRedirect(reverse('ventas'))
        
    else:
        form = AgregarVenta(user=user)

    return render(request, "main/ventas.html", {"form":form, "ventas":ventas})

@login_required
def boletas(request):

    return render(request, "main/boletas.html")

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