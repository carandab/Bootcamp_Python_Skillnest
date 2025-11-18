from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import TareaForm, RegistroForm
from django.contrib.auth.forms import AuthenticationForm

# Almacenamiento en memoria: diccionario donde la clave es el user_id
# y el valor es una lista de diccionarios con las tareas
TAREAS_MEMORIA = {}

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Cuenta creada para {username}')
            return redirect('login')
    else:
        form = RegistroForm()
    return render(request, 'registro/signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Bienvenido {username}!')
                return redirect('lista_tareas')
            else:
                messages.error(request, 'Usuario o contraseña incorrectos.')
        else:
            messages.error(request, 'Usuario o contraseña incorrectos.')
    else:
        form = AuthenticationForm()
    return render(request, 'registro/login.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.success(request, 'Has cerrado sesión exitosamente.')
    return redirect('index')

@login_required
def lista_tareas(request):
    user_id = request.user.id
    
    # Inicializar lista de tareas para el usuario si no existe
    if user_id not in TAREAS_MEMORIA:
        TAREAS_MEMORIA[user_id] = []
    
    tareas = TAREAS_MEMORIA[user_id]
    return render(request, 'tareas/tareas_lista.html', {'tareas': tareas})

@login_required
def detalle_tarea(request, tarea_id):
    user_id = request.user.id
    
    # Verificar que el usuario tenga tareas
    if user_id not in TAREAS_MEMORIA:
        messages.error(request, 'Tarea no encontrada.')
        return redirect('lista_tareas')
    
    # Buscar la tarea por ID
    tareas = TAREAS_MEMORIA[user_id]
    tarea = None
    for t in tareas:
        if t['id'] == tarea_id:
            tarea = t
            break
    
    if tarea is None:
        messages.error(request, 'Tarea no encontrada.')
        return redirect('lista_tareas')
    
    return render(request, 'tareas/tareas_detalle.html', {'tarea': tarea})

@login_required
def agregar_tarea(request):
    if request.method == 'POST':
        form = TareaForm(request.POST)
        if form.is_valid():
            user_id = request.user.id
            
            # Inicializar lista si no existe
            if user_id not in TAREAS_MEMORIA:
                TAREAS_MEMORIA[user_id] = []
            
            # Generar ID único para la tarea
            if TAREAS_MEMORIA[user_id]:
                nuevo_id = max(t['id'] for t in TAREAS_MEMORIA[user_id]) + 1
            else:
                nuevo_id = 1
            
            # Crear nueva tarea
            nueva_tarea = {
                'id': nuevo_id,
                'titulo': form.cleaned_data['titulo'],
                'descripcion': form.cleaned_data['descripcion'],
                'completada': False
            }
            
            TAREAS_MEMORIA[user_id].append(nueva_tarea)
            messages.success(request, 'Tarea creada exitosamente.')
            return redirect('lista_tareas')
    else:
        form = TareaForm()
    
    return render(request, 'tareas/tareas_agregar.html', {'form': form})

@login_required
def eliminar_tarea(request, tarea_id):
    user_id = request.user.id
    
    if user_id not in TAREAS_MEMORIA:
        messages.error(request, 'Tarea no encontrada.')
        return redirect('lista_tareas')
    
    # Buscar y eliminar la tarea
    tareas = TAREAS_MEMORIA[user_id]
    tarea_encontrada = None
    
    for i, t in enumerate(tareas):
        if t['id'] == tarea_id:
            tarea_encontrada = t
            if request.method == 'POST':
                tareas.pop(i)
                messages.success(request, 'Tarea eliminada exitosamente.')
                return redirect('lista_tareas')
            break
    
    if tarea_encontrada is None:
        messages.error(request, 'Tarea no encontrada.')
        return redirect('lista_tareas')
    
    return render(request, 'tareas/tareas_eliminar.html', {'tarea': tarea_encontrada})