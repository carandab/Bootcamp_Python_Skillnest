from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Evento
from .forms import EventoForm
from login.mixins import verificar_login, verificar_login_permiso
from django.contrib.auth.decorators import login_required

def inicio(request):
    if request.user.is_authenticated:
        eventos_registrados = Evento.objects.filter(participantes=request.user).order_by('fecha')
        otros_eventos = Evento.objects.exclude(participantes=request.user).order_by('fecha')[:6]
        eventos = list(eventos_registrados) + list(otros_eventos)
    else:
        eventos = Evento.objects.all().order_by('-fecha')[:6]  # Mostrar solo los 6 más recientes
    return render(request, 'inicio.html', {'eventos': eventos})

def crear_evento(request):
    # Lógica para crear un nuevo evento (requiere permiso personalizado)
    resultado = verificar_login_permiso(request, 'login.crear_eventos')
    if resultado:
        return resultado
    
    if request.method == 'POST':
        form = EventoForm(request.POST, request.FILES)
        if form.is_valid():
            # Crear evento usando ModelForm
            evento = form.save(commit=False)
            evento.creador = request.user
            evento.save()
            messages.success(request, 'Evento creado con éxito.')
            return redirect('app_eventos:lista_eventos')
    else:
        form = EventoForm()
    return render(request, 'crear_evento.html', {'form': form})

def lista_eventos(request):
    # Lógica para obtener y mostrar la lista de eventos - accesible para todos
    eventos = Evento.objects.all().order_by('-fecha')
    return render(request, 'lista_eventos.html', {'eventos': eventos})

def editar_evento(request, evento_id):
    # Lógica para editar un evento existente (requiere permiso personalizado)
    resultado = verificar_login_permiso(request, 'login.editar_eventos')
    if resultado:
        return resultado

    evento = get_object_or_404(Evento, id=evento_id)
    
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            # Usar ModelForm para guardar cambios
            evento_actualizado = form.save(commit=False)
            evento_actualizado.creador = request.user
            evento_actualizado.save()
            messages.success(request, f'Evento editado con éxito: {evento_actualizado.nombre}.')
            return redirect('app_eventos:lista_eventos')
        else:
            messages.error(request, 'Error al editar el evento.')
    else:
        # Usar instance para prellenar el formulario
        form = EventoForm(instance=evento)

    return render(request, 'editar_evento.html', {'form': form, 'evento': evento})

def eliminar_evento(request, evento_id):
    # Lógica para eliminar un evento existente (requiere permiso personalizado)
    resultado = verificar_login_permiso(request, 'login.eliminar_eventos')
    if resultado:
        return resultado

    evento = get_object_or_404(Evento, id=evento_id)

    if request.method == 'POST':
        evento.delete()
        messages.success(request, 'Evento eliminado con éxito.')
        return redirect('app_eventos:lista_eventos')
    return render(request, 'eliminar_evento.html', {'evento': evento})

def detalle_evento(request, evento_id):
    """Vista para mostrar el detalle de un evento individual."""
    evento = get_object_or_404(Evento, id=evento_id)
    return render(request, 'detalle_evento.html', {'evento': evento})

def registrar_evento(request, evento_id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión para registrarte en un evento.')
        return redirect('auth:register')
    evento = get_object_or_404(Evento, id=evento_id)
    if evento.participantes.count() < evento.capacidad:
        evento.participantes.add(request.user)
        messages.success(request, f'Te has registrado en el evento "{evento.nombre}".')
    else:
        messages.error(request, 'El evento ya ha alcanzado su capacidad máxima.')
    return redirect('app_eventos:detalle_evento', evento_id=evento.id)

def cancelar_registro_evento(request, evento_id):
    if not request.user.is_authenticated:
        messages.info(request, 'Debes iniciar sesión para cancelar tu registro en un evento.')
        return redirect('auth:login')
    evento = get_object_or_404(Evento, id=evento_id)
    evento.participantes.remove(request.user)
    messages.success(request, f'Has cancelado tu registro en el evento "{evento.nombre}".')
    return redirect('app_eventos:detalle_evento', evento_id=evento.id)
