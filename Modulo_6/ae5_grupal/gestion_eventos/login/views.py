from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission
from django.contrib.contenttypes.models import ContentType
from django.contrib import messages
from .models import CustomUser

# Create your views here.
def register_view(request):
    class CustomUserCreationForm(UserCreationForm):
        class Meta:
            model = CustomUser
            fields = ('username', 'email', 'first_name', 'last_name', 'password1', 'password2')
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Asignar al grupo de asistentes por defecto
            group, _ = Group.objects.get_or_create(name='asistentes')

            # Asegurar permisos personalizados asignados al grupo de asistentes
            # Los permisos están definidos en login.CustomUser (app_label='login')
            perms_needed = ['ver_eventos']  # Los asistentes solo necesitan permiso para ver eventos

            for codename in perms_needed:
                try:
                    perm = Permission.objects.get(codename=codename, content_type__app_label='login')
                    group.permissions.add(perm)
                except Permission.DoesNotExist:
                    # Si aún no existen (p.ej., migraciones no aplicadas), continuar sin romper registro
                    pass

            user.groups.add(group)
            login(request, user)  # Log the user in after registration
            # Obtener la URL de redirección del parámetro next o usar la página de inicio por defecto
            next_url = request.GET.get('next')
            if next_url:
                return redirect(next_url)
            return redirect('app_eventos:inicio')
    else:
        form = CustomUserCreationForm()
    return render(request, 'register.html', {'form': form})


def login_view(request):
    username = ''
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '')
        
        # Validaciones básicas
        if not username:
            messages.error(request, 'Por favor ingresa tu nombre de usuario.')
            return render(request, 'login.html', {'username': username})
        
        if not password:
            messages.error(request, 'Por favor ingresa tu contraseña.')
            return render(request, 'login.html', {'username': username})
        
        # Verificar si el usuario existe
        try:
            user_obj = CustomUser.objects.get(username=username)
        except CustomUser.DoesNotExist:
            messages.error(request, f'El usuario "{username}" no existe.')
            return render(request, 'login.html', {'username': username})
        
        # Verificar si está activo
        if not user_obj.is_active:
            messages.error(request, 'Tu cuenta está inactiva. Contacta al administrador.')
            return render(request, 'login.html', {'username': username})
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        if user is not None:
            # Verificar acceso admin si viene del admin
            next_url = request.GET.get('next', '')
            if '/admin/' in next_url and not user.is_staff:
                messages.error(request, 'No tienes permisos para acceder al área administrativa.')
                return render(request, 'login.html', {'username': username})
            
            login(request, user)
            messages.success(request, f'¡Bienvenido {username}!')
            
            # Redirigir
            if next_url:
                return redirect(next_url)
            else:
                return redirect('app_eventos:inicio')
        else:
            messages.error(request, f'Contraseña incorrecta para "{username}".')
            return render(request, 'login.html', {'username': username})
    
    return render(request, 'login.html', {'username': username})

def logout_view(request):
    username = request.user.username if request.user.is_authenticated else None
    
    # Limpiar mensajes previos antes del logout
    storage = messages.get_messages(request)
    for _ in storage:
        pass  # Esto consume/limpia los mensajes anteriores
    
    logout(request)
    
    # Agregar solo el mensaje de despedida
    if username:
        messages.success(request, f'¡Hasta luego, {username}! Has cerrado sesión correctamente.')
    else:
        messages.info(request, 'Has cerrado sesión correctamente.')
    
    return redirect('auth:login')
