from django.shortcuts import render, get_object_or_404
from .models import Receta

def inicio(request):
    return render(request, 'inicio.html')

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista_recetas.html', {'recetas': recetas})

def contacto(request):
    return render(request, 'contacto.html')

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'detalle_receta.html', {'receta': receta})
