from django.db import models
from products.models import Product
from django.contrib.auth.models import User

# Órdenes

class Order(models.Model):

    # Estados posibles de una orden
    STATUS_CHOICES = [
        ('Pending', 'Pendiente'),
        ('Processing', 'En Proceso'),
        ('Shipped', 'Enviado'),
        ('Delivered', 'Entregado'),
        ('Cancelled', 'Cancelado'),
    ]

    # Información de la orden
    status = models.CharField(max_length=50, default='Pending')
    total = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00,
        verbose_name='Total de la Orden'
        )
    shipping_address = models.TextField(verbose_name='Dirección de Envío')
    billing_address = models.TextField(
        blank=True,
        help_text='Dejar vacío si es igual a la dirección de envío',
        verbose_name='Dirección de Facturación')
    
    notes = models.TextField(blank=True, null=True, verbose_name='Notas Adicionales')


    #Relaciones

    # Relacion con user (Cliente) (ForeignKey 1:N)
    customer = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='orders',
        verbose_name='Cliente'
    )

    # Relacion con productos (ManyToMany N:M) a través de OrderItem
    products = models.ManyToManyField(
        Product,
        through='OrderItem',
        related_name='orders',
        verbose_name='Productos'
    )


    # Fechas 
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Pedido'
        verbose_name_plural = 'Pedidos'
        ordering = ['-created_at']

    def __str__(self):
        return f"Pedido {self.id} - {self.customer.username}"
    
    # Método para calcular el total de la orden
    def calculate_total(self):

        total = sum(item.subtotal for item in self.items.all())
        self.total = total
        self.save()

        return total
    
    def save(self, *args, **kwargs):
        # Si billing_address está vacío, usar shipping_address
        if not self.billing_address:
            self.billing_address = self.shipping_address
        super().save(*args, **kwargs)

class OrderItem(models.Model):

    # Relaciones

    # Relación con Orden
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name='Orden'
    )
    # Relación con Producto
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='order_items',
        verbose_name='Producto'
    )

    
    quantity = models.PositiveIntegerField(
        default=1,
        verbose_name='Cantidad'
    )

    unit_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Precio por Unidad'
    )

    subtotal = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name='Subtotal',
        editable=False
    )

    class Meta:
        verbose_name = 'Item de Pedido'
        verbose_name_plural = 'Items de Pedido'
        unique_together = ('order', 'product')

    # Método para calcular el subtotal
    def save(self, *args, **kwargs):

        self.subtotal = self.quantity * self.unit_price
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity}x {self.product.name} (Pedido #{self.order.id})"