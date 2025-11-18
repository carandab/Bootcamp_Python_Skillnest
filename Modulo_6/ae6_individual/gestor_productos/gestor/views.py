from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.views.generic import TemplateView
from django.contrib.auth.models import Group
from .models import Producto, CustomUser
from .forms import ProductoForm, CustomUserCreationForm
from .mixins import (CustomLoginRequiredMixin, CustomPermissionRequiredMixin, ProtectedTemplateView, PermissionProtectedTemplateView)

# Index

class IndexView(TemplateView):
    template_name = 'index.html'
    
    # Contexto adicional
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Agregar información útil al contexto
        if self.request.user.is_authenticated:
            context['user_groups'] = self.request.user.groups.all()
            context['productos_count'] = Producto.objects.count()
        return context

# Vista del Registro de Usuario

def RegisterView(request):
    
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            
            # Asignar grupo
            group_name = request.POST.get('group')
            if group_name:
                try:
                    group = Group.objects.get(name=group_name)
                    user.groups.add(group)
                    messages.success(
                        request, 
                        f'Usuario "{user.username}" creado y agregado al grupo "{group_name}"'
                    )
                except Group.DoesNotExist:
                    messages.warning(
                        request, 
                        f'Usuario creado pero el grupo "{group_name}" no existe'
                    )
            else:
                messages.success(request, f'Usuario "{user.username}" creado exitosamente')
            
            # Iniciar sesión automáticamente
            login(request, user)
            return redirect('index')
        else:
            # Mostrar errores específicos
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
    else:
        form = CustomUserCreationForm()
    
    # Obtener grupos disponibles con el ORM
    groups = Group.objects.all()
    
    return render(request, 'register.html', {
        'form': form,
        'groups': groups
    })

# Vista del Login

class LoginView(TemplateView):
    template_name = 'login.html'

    def get(self, request, *args, **kwargs):
        # Si ya está autenticado, redirigir al index
        if request.user.is_authenticated:
            messages.info(request, f'Ya has iniciado sesión como {request.user.username}')
            return redirect('index')
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        # Validar que se ingresaron credenciales
        if not username or not password:
            messages.error(request, 'Por favor ingresa usuario y contraseña')
            return render(request, self.template_name)
        
        # Autenticar usuario
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            # Usuario autenticado correctamente
            login(request, user)
            
            # Mensaje de bienvenida personalizado
            groups = user.groups.all()
            if groups:
                group_names = ', '.join([g.name for g in groups])
                messages.success(
                    request, 
                    f'¡Bienvenido {user.username}! Grupos: {group_names}'
                )
            else:
                messages.success(request, f'¡Bienvenido {user.username}!')
            
            # Redirigir a la página solicitada o al index
            next_url = request.GET.get('next', 'index')
            return redirect(next_url)
        else:
            # Credenciales incorrectas
            messages.error(request, 'Usuario o contraseña incorrectos')
            return render(request, self.template_name, {
                'error': 'Usuario o contraseña incorrectos',
                'username': username  # Mantener el usuario ingresado
            })

# Vista del Logout

def LogoutView(request):

    if request.user.is_authenticated:
        username = request.user.username
        logout(request)
        messages.info(request, f'Sesión cerrada. ¡Hasta pronto, {username}!')
    else:
        messages.warning(request, 'No había ninguna sesión activa')
    
    return render(request, 'logout.html')

# CRUD

# Ver

class ProductoListView(PermissionProtectedTemplateView):

    template_name = 'producto_list.html'
    permission_required = 'gestor.view_producto'

    def get(self, request, *args, **kwargs):

        # Obtener todos los productos ordenados por fecha
        productos = Producto.objects.all().order_by('-fecha_creacion')
        
        # Verificar permisos del usuario para mostrar botones
        can_add = request.user.has_perm('gestor.add_producto')
        can_change = request.user.has_perm('gestor.change_producto')
        can_delete = request.user.has_perm('gestor.delete_producto')
        
        return render(request, self.template_name, {
            'productos': productos,
            'can_add': can_add,
            'can_change': can_change,
            'can_delete': can_delete,
        })

# Agregar

class ProductoAddView(PermissionProtectedTemplateView):
    template_name = 'producto_add.html'
    permission_required = 'gestor.add_producto'

    def get(self, request, *args, **kwargs):
        form = ProductoForm()
        return render(request, self.template_name, {
            'form': form,
            'action': 'Crear',
        })

    def post(self, request, *args, **kwargs):
        form = ProductoForm(request.POST)
        if form.is_valid():
            producto = form.save()
            messages.success(
                request, 
                f'✅ Producto "{producto.nombre}" creado exitosamente'
            )
            return redirect('productos')
        else:
            # Mostrar errores específicos
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
        
        return render(request, self.template_name, {
            'form': form,
            'action': 'Crear',
        })


# Actualizar

class ProductoUpdateView(PermissionProtectedTemplateView):

    template_name = 'producto_update.html'
    permission_required = 'gestor.change_producto'

    def get(self, request, pk, *args, **kwargs):
        producto = get_object_or_404(Producto, pk=pk)
        form = ProductoForm(instance=producto)
        return render(request, self.template_name, {
            'form': form,
            'producto': producto,
            'action': 'Actualizar',
        })

    def post(self, request, pk, *args, **kwargs):
        producto = get_object_or_404(Producto, pk=pk)
        form = ProductoForm(request.POST, instance=producto)
        
        if form.is_valid():
            producto = form.save()
            messages.success(
                request, 
                f'✅ Producto "{producto.nombre}" actualizado exitosamente'
            )
            return redirect('productos')
        else:
            # Mostrar errores específicos
            for field, errors in form.errors.items():
                for error in errors:
                    messages.error(request, f'{field}: {error}')
        
        return render(request, self.template_name, {
            'form': form,
            'producto': producto,
            'action': 'Actualizar',
        })


# Eliminar

class ProductoDeleteView(PermissionProtectedTemplateView):

    template_name = 'producto_delete.html'
    permission_required = 'gestor.delete_producto'

    def get(self, request, pk, *args, **kwargs):
        producto = get_object_or_404(Producto, pk=pk)
        return render(request, self.template_name, {
            'producto': producto
        })

    def post(self, request, pk, *args, **kwargs):
        producto = get_object_or_404(Producto, pk=pk)
        nombre = producto.nombre
        producto.delete()
        messages.success(
            request, 
            f'🗑️ Producto "{nombre}" eliminado exitosamente'
        )
        return redirect('productos')


# Manejo de Errores

def handler403(request, exception=None):
    """Manejador personalizado para errores 403 (Permiso denegado)
    /// No se puede acceder a la página sin permiso de acceso /// """

    return render(request, '403.html', status=403)


def handler404(request, exception=None):
    """Manejador personalizado para errores 404 (Página no encontrada)
    /// URL no encontrada /// """

    return render(request, '404.html', status=404)