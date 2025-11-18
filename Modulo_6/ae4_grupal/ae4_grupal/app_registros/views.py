from django.shortcuts import render
from .forms import EventoForm, ParticipanteForm 

def inicio(request):
    return render(request, 'inicio.html')

def registrar_evento(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            # Procesar datos
            nombre = form.cleaned_data['nombre']
            fecha = form.cleaned_data['fecha']
            ubicacion = form.cleaned_data['ubicacion']
            # Realizar alguna acción con los datos, como enviar un correo
            return render(request, 'formulario_exito.html', {'nombre': nombre})
    else:
        form = EventoForm()
    
    return render(request, 'formulario1.html', {'form': form})

def registrar_persona(request):
    if request.method == 'POST':
        form = ParticipanteForm(request.POST)
        if form.is_valid():
            # Procesar datos
            nombre = form.cleaned_data['nombre']
            correo = form.cleaned_data['correo']
            # Realizar algunaacción con los datos, como enviar un correo
            return render(request, 'formulario_exito.html', {'nombre': nombre})
    else:
        form = ParticipanteForm()
    
    return render(request, 'formulario2.html', {'form': form})

