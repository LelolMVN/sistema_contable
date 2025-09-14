from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Boletas
from .forms import CrearBoleta
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'main/index.html', {})

@login_required
def ventas(request):
    boletas = Boletas.objects.all()

    return render(request, "main/ventas.html", {"boletas":boletas})

@login_required
def boletas(request):
    boletas = Boletas.objects.all()

    if request.method == "POST":
        form = CrearBoleta(request.POST)
        if form.is_valid():
            cliente = form.cleaned_data["cliente"]
            total = form.cleaned_data["total"]
            detalle = form.cleaned_data["detalle"]
            boleta = Boletas(user = request.user, cliente=cliente, total=total, detalle=detalle)
            boleta.save()

            return HttpResponseRedirect(reverse('boletas'))
        
    else:
        form = CrearBoleta()

    return render(request, "main/boletas.html", {"form":form, "boletas":boletas})

'''
def index(request, nombre):
    producto = Productos.objects.get(nombre=nombre)
    venta = Ventas.objects.get(id=1)

    dict = {
    "producto": producto.nombre
    }
    return render(request, 'main/index.html', dict)
'''