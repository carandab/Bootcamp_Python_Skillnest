from django.db import models
from django.contrib.auth.models import User


class CustomerProfile(models.Model):


    # Herencia del modelo User de Django

    user = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        related_name='cliente_profile'
    )
    # Información adicional del cliente
    phone = models.CharField(max_length=15, blank=True)

    # Información para envíos y facturación
    address = models.TextField(blank=True)
    city = models.CharField(max_length=100, blank=True)
    postal_code = models.CharField(max_length=10, blank=True)

    # Fechas importantes
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Perfil de Cliente'
        verbose_name_plural = 'Perfiles de Clientes'


    def __str__(self):
        return f"Perfil de {self.user.username}"