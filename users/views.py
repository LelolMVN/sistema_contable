from django.shortcuts import render, redirect
from .forms import CrearUsuario

def registro(request):
    if request.method == "POST":
        form = CrearUsuario(request.POST)
        if form.is_valid():
            form.save()
        
        return redirect('index')
    else:
        form = CrearUsuario()

    return render(request, 'users/registro.html', {"form": form})


'''
from django.shortcuts import render, redirect
from .forms import CrearUsuario
from main.models import Bodegas

def registro(request):
    if request.method == "POST":
        form = CrearUsuario(request.POST)

        if form.is_valid():
            user = form.save()
            bodega = Bodegas(user=user, bodega="Bodega1")

            bodega.save()

        return redirect('index')
    
    else:
        form = CrearUsuario()

    return render(request, 'users/registro.html', {"form": form})
'''