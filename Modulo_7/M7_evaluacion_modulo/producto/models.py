from django.db import models
from categorias.models import Categoria
from etiquetas.models import Etiqueta


class DetallesProducto(models.Model):

        
    # Relación Uno a Uno
    producto = models.OneToOneField(
        'Producto',
        on_delete=models.CASCADE,
        related_name='detalles',
        primary_key=True
    )

    # Campos

    peso = models.DecimalField(
        max_digits=8, 
        decimal_places=2, 
        help_text="Peso en kg",
        null=True,
        blank=True
    )
    dimensiones = models.CharField(
        max_length=100, 
        blank=True, 
        help_text="Ej: 10x20x5 cm"
    )
    
    class Meta:
        verbose_name = "Detalle del Producto"
        verbose_name_plural = "Detalles de Productos"

    def __str__(self):
        return f"Detalles (Peso: {self.peso or 'N/A'} kg)"


class Producto(models.Model):

    # Campos

    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    
    # Relación Muchos a Uno
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.PROTECT,
        related_name='productos'
    )

    # Relación Muchos a Muchos
    etiquetas = models.ManyToManyField(
        Etiqueta, 
        through='ProductoEtiqueta', 
        related_name='productos'
    )
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ['-created_at', '-updated_at', 'nombre', 'categoria', 'precio']

    def __str__(self):
        return self.nombre


#  Modelo intermedio para la relación Many-to-Many

class ProductoEtiqueta(models.Model):


    producto = models.ForeignKey(
        Producto, 
        on_delete=models.CASCADE,
        related_name='producto_etiquetas'
    )

    etiqueta = models.ForeignKey(
        Etiqueta, 
        on_delete=models.CASCADE,
        related_name='producto_etiquetas'
    )
    
    # Campos adicionales de la relación
    fecha_asignacion = models.DateTimeField(auto_now_add=True)
    # Campo de orden para prioridad de las etiquetas
    orden = models.PositiveIntegerField(
        default= 1,
        help_text="Orden de prioridad de la etiqueta (1 = más importante)"
    )
    
    class Meta:
        verbose_name = "Producto-Etiqueta"
        verbose_name_plural = "Productos-Etiquetas"
        unique_together = ('producto', 'etiqueta') # Evita duplicados cuando se asigne una etiqueta a un producto
        ordering = ['orden', 'fecha_asignacion']
    
    def __str__(self):
        return f"{self.producto.nombre} - {self.etiqueta.nombre}"