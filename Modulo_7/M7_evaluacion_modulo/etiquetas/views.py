from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Etiqueta
from .forms import EtiquetaForm


def lista_etiquetas(request):
    etiquetas = Etiqueta.objects.all()
    return render(request, 'etiquetas/lista.html', {'etiquetas': etiquetas})


def crear_etiqueta(request):
    if request.method == 'POST':
        form = EtiquetaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta creada exitosamente')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm()
    
    return render(request, 'etiquetas/formulario.html', {'form': form, 'accion': 'Crear'})


def editar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        form = EtiquetaForm(request.POST, instance=etiqueta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Etiqueta actualizada exitosamente')
            return redirect('lista_etiquetas')
    else:
        form = EtiquetaForm(instance=etiqueta)
    
    return render(request, 'etiquetas/formulario.html', {
        'form': form,
        'accion': 'Editar',
        'etiqueta': etiqueta
    })


def eliminar_etiqueta(request, id):
    etiqueta = get_object_or_404(Etiqueta, id=id)
    
    if request.method == 'POST':
        etiqueta.delete()
        messages.success(request, 'Etiqueta eliminada exitosamente')
        return redirect('lista_etiquetas')
    
    return render(request, 'etiquetas/eliminar.html', {'etiqueta': etiqueta})