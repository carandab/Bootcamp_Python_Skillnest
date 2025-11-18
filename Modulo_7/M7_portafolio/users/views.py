from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from .models import CustomerProfile

# Registro de nuevo usuario

def register(request):

    if request.method == 'POST':
        form = UserCreationForm(request.POST)               # Formulario de creación de usuario de Django
        if form.is_valid():
            try:
                with transaction.atomic():
                    user = form.save()
                    
                    # Crear perfil automáticamente
                    CustomerProfile.objects.create(user=user)
                    
                    # Login automático
                    login(request, user)
                    
                    messages.success(request, '¡Cuenta creada exitosamente!')
                    return redirect('products:index')
                
            except Exception as e:
                messages.error(request, f'Error al crear la cuenta: {str(e)}')

        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')

    else:
        form = UserCreationForm()
    
    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    profile = getattr(request.user, 'cliente_profile', None)
    
    return render(request, 'users/profile.html', {
        'profile': profile
    })


@login_required
def profile_edit(request):

    profile, created = CustomerProfile.objects.get_or_create(user=request.user)
    
    if request.method == 'POST':
        
        # Actualizar datos del usuario
        request.user.first_name = request.POST.get('first_name', '').strip()
        request.user.last_name = request.POST.get('last_name', '').strip()
        request.user.email = request.POST.get('email', '').strip()
        request.user.save()
        
        # Actualizar perfil
        profile.phone = request.POST.get('phone', '').strip()
        profile.address = request.POST.get('address', '').strip()
        profile.city = request.POST.get('city', '').strip()
        profile.postal_code = request.POST.get('postal_code', '').strip()
        profile.save()
        
        messages.success(request, 'Perfil actualizado exitosamente.')
        return redirect('users:profile')
    
    return render(request, 'users/profile_edit.html', {
        'profile': profile
    })