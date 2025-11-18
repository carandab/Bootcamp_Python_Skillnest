from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import CustomerProfile

class CustomerProfileInline(admin.StackedInline):

    model = CustomerProfile
    can_delete = False
    verbose_name = 'Perfil de Cliente'
    verbose_name_plural = 'Perfil de Cliente'
    
    fields = [
        'phone',
        'address',
        'city',
        'postal_code',
    ]
    
    # Solo mostrar para usuarios que NO son staff
    def has_add_permission(self, request, obj=None):
        # Si el usuario es staff, no mostrar el inline
        if obj and obj.is_staff:
            return False
        return super().has_add_permission(request, obj)
    
class CustomUserAdmin(BaseUserAdmin):


    inlines = [CustomerProfileInline]
    
    # Columnas visibles en la lista
    list_display = [
        'username',
        'email',
        'first_name',
        'last_name',
        'is_staff',
        'is_active',
        'date_joined'
    ]
    
    # Filtros
    list_filter = [
        'is_staff',
        'is_superuser',
        'is_active',
        'date_joined'
    ]
    
    # Búsqueda
    search_fields = [
        'username',
        'email',
        'first_name',
        'last_name'
    ]
    
    # Orden
    ordering = ['-date_joined']

@admin.register(CustomerProfile)
class CustomerProfileAdmin(admin.ModelAdmin):


    list_display = [
        'user',
        'phone',
        'city',
    ]
    
    search_fields = [
        'user__username',
        'user__email',
        'user__first_name',
        'user__last_name',
        'phone',
        'city'
    ]
    
    list_filter = [
        'city',
    ]
    
    readonly_fields = ['created_at', 'updated_at']
    
    fieldsets = (
        ('Usuario', {
            'fields': ('user',)
        }),
        ('Contacto', {
            'fields': ('phone',)
        }),
        ('Dirección', {
            'fields': ('address', 'city', 'postal_code')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

# Re-registrar el modelo User con la nueva configuración
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)