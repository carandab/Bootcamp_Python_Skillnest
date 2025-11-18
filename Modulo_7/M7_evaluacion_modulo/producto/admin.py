from django.contrib import admin
from .models import Producto, DetallesProducto, ProductoEtiqueta


class DetallesProductoInline(admin.StackedInline):

    model = DetallesProducto
    extra = 0
    can_delete = False


class ProductoEtiquetaInline(admin.TabularInline):

    model = ProductoEtiqueta
    extra = 1
    fields = ('etiqueta', 'orden')


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'precio', 'categoria', 'created_at', 'cantidad_etiquetas')
    list_filter = ('categoria', 'created_at')
    search_fields = ('nombre', 'descripcion')
    inlines = [DetallesProductoInline, ProductoEtiquetaInline]
    readonly_fields = ('created_at', 'updated_at')
    
    def cantidad_etiquetas(self, obj):
        return obj.etiquetas.count()
    
    cantidad_etiquetas.short_description = 'Etiquetas'


@admin.register(ProductoEtiqueta)
class ProductoEtiquetaAdmin(admin.ModelAdmin):

    list_display = ('producto', 'etiqueta', 'orden', 'fecha_asignacion')
    list_filter = ('etiqueta', 'fecha_asignacion')
    search_fields = ('producto__nombre', 'etiqueta__nombre')
