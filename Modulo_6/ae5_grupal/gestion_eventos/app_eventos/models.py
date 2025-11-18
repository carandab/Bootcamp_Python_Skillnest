from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

# Create your models here
class Evento(models.Model):
    nombre = models.CharField(max_length=200)
    fecha = models.DateField()
    hora = models.TimeField(blank=True, null=True)
    ubicacion = models.CharField(max_length=200)
    capacidad = models.PositiveIntegerField(blank=True, null=True)
    descripcion = models.TextField(blank=True, null=True)
    creador = models.ForeignKey(User, on_delete=models.CASCADE)
    participantes = models.ManyToManyField(User, related_name='eventos_registrados', blank=True)

    def __str__(self):
        return self.nombre
