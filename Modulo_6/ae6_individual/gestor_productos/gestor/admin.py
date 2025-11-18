from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django import forms
from .models import Producto, CustomUser


# Formulario personalizado para agregar productos en admin

class ProductoAdminForm(forms.ModelForm):
    
    class Meta:
        model = Producto
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'vTextField',
                'placeholder': 'Ingrese el nombre del producto',
                'style': 'width: 400px;'
            }),
            'descripcion': forms.Textarea(attrs={
                'rows': 4,
                'cols': 80,
                'placeholder': 'Descripción detallada del producto...',
                'style': 'resize: vertical;'
            }),
            'precio': forms.NumberInput(attrs={
                'class': 'vTextField',
                'placeholder': '0.00',
                'step': '0.01',
                'min': '0'
            }),
            'stock': forms.NumberInput(attrs={
                'class': 'vIntegerField',
                'placeholder': '0',
                'min': '0',
                'style': 'width: 100px;'
            }),
        }
        help_texts = {
            'precio': 'Ingrese el precio en pesos chilenos (CLP)',
            'stock': 'Cantidad disponible en inventario',
        }


# Productos admin

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """Configuración del admin para el modelo Producto"""
    
    form = ProductoAdminForm
    
    # Campos que se muestran en la lista
    list_display = ('nombre', 'precio', 'stock', 'stock_status', 'fecha_creacion')
    
    # Filtros laterales
    list_filter = ('fecha_creacion',)
    
    # Campos de búsqueda
    search_fields = ('nombre', 'descripcion')
    
    # Ordenamiento por defecto
    ordering = ('-fecha_creacion',)
    
    # Campos de solo lectura
    readonly_fields = ('fecha_creacion',)
    
    # Organizar campos en secciones
    fieldsets = (
        ('Información Básica', {
            'fields': ('nombre', 'descripcion')
        }),
        ('Datos Comerciales', {
            'fields': ('precio', 'stock'),
            'description': 'Información sobre precio y disponibilidad del producto'
        }),
        ('Metadatos', {
            'fields': ('fecha_creacion',),
            'classes': ('collapse',)  # Sección colapsable
        }),
    )
    
    # Método personalizado para mostrar estado del stock
    def stock_status(self, obj):
        """Muestra el estado del stock con emojis"""
        if obj.stock == 0:
            return '🔴 Sin stock'
        elif obj.stock < 10:
            return '🟡 Stock bajo'
        else:
            return '🟢 Disponible'
    stock_status.short_description = 'Estado'
    
    # Control de permisos para eliminar
    def has_delete_permission(self, request, obj=None):
        """Solo superusuarios o miembros del grupo Administradores pueden eliminar"""
        if request.user.is_superuser:
            return True
        return request.user.groups.filter(name='Administradores').exists()


# Custom user admin

@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """
    Configuración del admin para CustomUser
    Extiende UserAdmin para mantener toda la funcionalidad de usuarios
    """
    
    # Campos que se muestran en la lista de usuarios
    list_display = ('username', 'email', 'first_name', 'last_name', 'is_staff', 'is_active', 'get_groups')
    
    # Filtros laterales
    list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
    
    # Campos de búsqueda
    search_fields = ('username', 'first_name', 'last_name', 'email')
    
    # Ordenamiento
    ordering = ('username',)
    
    # Método personalizado para mostrar grupos
    def get_groups(self, obj):
        """Muestra los grupos del usuario"""
        groups = obj.groups.all()
        if groups:
            return ', '.join([group.name for group in groups])
        return '-'
    get_groups.short_description = 'Grupos'
    
    # Organización de campos en el formulario de edición
    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Información Personal', {
            'fields': ('first_name', 'last_name', 'email')
        }),
        ('Permisos', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions'),
        }),
        ('Fechas Importantes', {
            'fields': ('last_login', 'date_joined'),
            'classes': ('collapse',)
        }),
    )
    
    # Campos para crear un nuevo usuario
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'email', 'password1', 'password2'),
        }),
        ('Información Personal', {
            'fields': ('first_name', 'last_name'),
        }),
        ('Permisos', {
            'fields': ('is_staff', 'is_active', 'groups'),
        }),
    )


# Personalizar títulos del sitio admin
admin.site.site_header = "Gestión de Productos - Administración"
admin.site.site_title = "Panel de Administración"
admin.site.index_title = "Bienvenido al Panel de Administración"