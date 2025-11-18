from django.db import models

class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=5, decimal_places=2)
    disponible = models.BooleanField()

    class Meta:
        # Index para el campo 'nombre' para mejorar la eficiencia de búsqueda en ORM
        indexes = [
            models.Index(fields=['nombre'], name='nombre_idx'),
        ]