from django.contrib import admin
from .models import CustomUser

#Personalizar el sitio de administración con titulos descriptivos
admin.site.site_header = "Administración de Gestión de Eventos"
admin.site.site_title = "Panel de Administración de Gestión de Eventos"
admin.site.index_title = "Bienvenido al Panel de Administración de Gestión de Eventos"

# Personalizar la vista de administración de usuarios
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'first_name', 'last_name', 'get_groups', 'is_staff')
    list_filter = ('groups', 'is_staff', 'is_active')
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ('groups', 'user_permissions',)

    def get_groups(self, obj):
        """Obtener los grupos del usuario en formato legible"""
        return ", ".join([group.name for group in obj.groups.all()])
    get_groups.short_description = 'Grupos'

