from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction, IntegrityError
from django.contrib import messages
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm

# Voluntarios

def lista_voluntarios(request):
    voluntarios = Voluntario.objects.all().order_by('-id')
    return render(request, 'voluntarios/lista_voluntarios.html', {'voluntarios': voluntarios})

def detalle_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    return render(request, 'voluntarios/voluntario_detalle.html', {'voluntario': voluntario})

def crear_voluntario(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    voluntario = form.save()
                messages.success(request, "Voluntario creado correctamente.")
                return redirect('gestor:lista_voluntarios')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al crear al voluntario.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = VoluntarioForm()
    return render(request, 'voluntarios/voluntario_form.html', {'form': form, 'accion': 'Crear'})

def actualizar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                messages.success(request, "Voluntario actualizado correctamente.")
                return redirect('gestor:lista_voluntarios')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al actualizar el voluntario.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'voluntarios/voluntario_form.html', {'form': form, 'accion': 'Actualizar'})

def confirmar_eliminar_voluntario(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        voluntario.delete()
        messages.success(request, "Voluntario eliminado.")
        return redirect('gestor:lista_voluntarios')
    return render(request, 'voluntarios/voluntario_confirm_delete.html', {'voluntario': voluntario})


# Eventos


def lista_eventos(request):
    eventos = Evento.objects.all().order_by('-fecha')
    return render(request, 'eventos/lista_eventos.html', {
        'eventos': eventos
    })

def detalle_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/detalle_evento.html', {
        'evento': evento
    })

def crear_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            try:
                with transaction.atomic():
                    evento = form.save()
                messages.success(request, "Evento creado correctamente.")
                return redirect('gestor:lista_eventos')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al crear el evento.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = EventoForm()
    return render(request, 'eventos/evento_form.html', {
        'form': form, 
        'accion': 'Crear'
    })

def actualizar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            try:
                with transaction.atomic():
                    form.save()
                messages.success(request, "Evento actualizado correctamente.")
                return redirect('gestor:lista_eventos')
            except IntegrityError:
                messages.error(request, "Ocurrió un error al actualizar el evento.")
        else:
            messages.error(request, "Corrige los errores en el formulario.")
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/evento_form.html', {
        'form': form, 
        'accion': 'Actualizar'
    })

def confirmar_eliminar_evento(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        messages.success(request, "Evento eliminado.")
        return redirect('gestor:lista_eventos')
    return render(request, 'eventos/evento_confirm_delete.html', {
        'evento': evento
    })