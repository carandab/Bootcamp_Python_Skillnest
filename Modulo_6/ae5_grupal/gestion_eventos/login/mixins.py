from django.shortcuts import redirect
from django.contrib import messages

def verificar_login_permiso(request, permiso_necesario):
    """
    Mixin para verificar si el usuario está autenticado y tiene el permiso necesario.
    Si no está autenticado, redirige a la página de login.
    Si no tiene el permiso, muestra un mensaje de error y redirige a la página principal.
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    if not request.user.has_perm(permiso_necesario):
        messages.error(request, "No tienes permiso para acceder a esta sección.")
        return redirect('app_eventos:inicio')  # Redirigir a la página principal u otra adecuada
    
    return None  # Indica que el usuario tiene acceso

def verificar_login(request):
    """
    Mixin para verificar si el usuario está autenticado.
    Si no está autenticado, redirige a la página de login.
    """
    if not request.user.is_authenticated:
        return redirect('auth:login')
    
    return None  # Indica que el usuario está autenticado