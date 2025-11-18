from django.contrib import admin
from .models import Product, Category, Brand

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'is_active']
    search_fields = ['name']
    list_filter = ['is_active']
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # Columnas visibles en la lista
    list_display = ['name', 'category', 'brand', 'price', 'stock', 'is_active']
    
    # Búsqueda 
    search_fields = ['name', 'description', 'sku']
    
    # Filtros laterales
    list_filter = ['category', 'brand', 'is_active', 'is_featured', 'created_at']
    
    # Campos editables desde la lista
    list_editable = ['price', 'stock', 'is_active']
    
    # Orden
    ordering = ['-created_at']
    
    # Campos de solo lectura
    readonly_fields = ['created_at', 'updated_at']
    
    # Organización en el formulario
    fieldsets = (
        ('Información Básica', {
            'fields': ('name', 'slug', 'sku', 'description')
        }),
        ('Precios y Stock', {
            'fields': ('price', 'sale_price', 'stock')
        }),
        ('Categorización', {
            'fields': ('category', 'brand')
        }),
        ('Media', {
            'fields': ('image',)
        }),
        ('Opciones', {
            'fields': ('is_active', 'is_featured')
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)  # Colapsado por defecto
        }),
    )