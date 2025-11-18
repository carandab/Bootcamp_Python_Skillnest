from django.db import models

class Receta(models.Model):
    nombre = models.CharField(max_length=100)
    ingredientes = models.TextField()
    descripcion = models.TextField(null=True, blank=True)
    instrucciones = models.TextField()
    tiempo_preparacion = models.IntegerField(help_text="En minutos")
    imagen = models.ImageField(upload_to='recetas/', null=True, blank=True)

    def __str__(self):
        return self.nombre
