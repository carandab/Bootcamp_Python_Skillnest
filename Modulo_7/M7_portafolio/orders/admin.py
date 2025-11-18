from django.contrib import admin
from django.contrib.admin import widgets
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):

    model = OrderItem
    extra = 1                       # Muestra 1 fila vacía para agregar
    fields = ['product', 'quantity', 'unit_price', 'subtotal']
    readonly_fields = ['subtotal']  # Subtotal se calcula automáticamente
    
    # Autocompletar producto cuando se escribe el nombre
    autocomplete_fields = ['product']


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    
    list_display = [
        'id',
        'customer',
        'status',
        'total',
        'item_count',               #   Método definido abajo
        'created_at'
    ]

    list_editable = ['status']

    search_fields = [
        'id',
        'customer__username',
        'customer__email',
        'customer__first_name',
        'customer__last_name'
    ]

    list_filter = ['status','created_at','updated_at']
    ordering = ['-created_at']
    readonly_fields = ['total', 'created_at', 'updated_at']
    autocomplete_fields = ['customer']

    fieldsets = (
        ('Información del Pedido', {
            'fields': ('customer', 'status')
        }),
        ('Direcciones', {
            'fields': ('shipping_address', 'billing_address'),
            'description': 'Direcciones de envío y facturación del cliente.'
        }),
        ('Notas', {
            'fields': ('notes',),
            'classes': ('collapse',) 
        }),
        ('Totales', {
            'fields': ('total',),
            'classes': ('collapse',)
        }),
        ('Fechas', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )

    inlines = [OrderItemInline]

    # Método para mostrar cantidad de items en el pedido (agregado en list_display)
    @admin.display(description='Items')
    def item_count(self, obj):

        return obj.items.count()
    


@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'order',
        'product',
        'quantity',
        'unit_price',
        'subtotal'
    ]
    
    search_fields = [
        'order__id',
        'product__name',
        'product__sku'
    ]
    
    list_filter = [
        'order__status',
        'order__created_at'
    ]
    
    ordering = ['-order__created_at']
    
    readonly_fields = ['subtotal']
    
    # Autocompletar para búsqueda rápida
    autocomplete_fields = ['order', 'product']