from django.shortcuts import render, get_object_or_404
from recetas.models import Receta

def inicio(request):
    ultimas_recetas = Receta.objects.order_by('-id')[:5]
    return render(request, 'inicio.html', {'ultimas_recetas': ultimas_recetas})

def lista_recetas(request):
    recetas = Receta.objects.all()
    return render(request, 'lista_recetas.html', {'recetas': recetas})

def contacto(request):
    return render(request, 'contacto.html')

def detalle_receta(request, receta_id):
    receta = get_object_or_404(Receta, id=receta_id)
    return render(request, 'detalle_receta.html', {'receta': receta})