from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Profesores(models.Model):
    nombre = models.CharField(max_length=255)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Profesor: {self.nombre}"
    
class Cursos(models.Model):
    nombre = models.CharField(max_length=255)
    profesor = models.ForeignKey(
        Profesores,
        on_delete=models.CASCADE
    )
    descripcion = models.CharField(max_length=255)

    def __str__(self):
        return f"Curso: {self.nombre}, Profesor: {self.profesor}"
    
class Estudiantes(models.Model):

    nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    cursos = models.ManyToManyField(
        Cursos,
        through='Inscripciones',
        related_name='estudiantes'
    )

    def __str__(self):
        return f"Nombre: {self.nombre}"
    
class Inscripciones(models.Model):
    
    estudiante = models.ForeignKey(
        Estudiantes,
        on_delete=models.CASCADE
    )
    curso = models.ForeignKey(
        Cursos,
        on_delete=models.CASCADE
    )
    fecha_inscripcion = models.DateTimeField(auto_now_add=True)
    estado = models.CharField(
        max_length=20,
        choices=[('activo','Activo'), ('finalizado','Finalizado')],
        default='activo'
    )
    nota_final = models.DecimalField(
        max_digits=3,
        decimal_places=2,
        blank=True,
        null=True,
        validators=[MinValueValidator(1.0), MaxValueValidator(7.0)]
    )
    def __str__(self):
        return f"{self.estudiante} inscrito en {self.curso}"
    
class Perfiles(models.Model):

    estudiante = models.OneToOneField(
        Estudiantes,
        on_delete=models.CASCADE,
        related_name='perfil'
    )

    biografia = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    foto = models.ImageField(
        upload_to='media/imgs/',
        blank=True,
        null=True
    )

    redes = models.URLField(
        blank=True,
        null=True
    )
    
    def __str__(self):
        return f"Perfil de {self.estudiante}"
    
""" En caso de querer separarlas

    linkedin = models.URLField(
        blank=True,
        null=True
    )
    github= models.URLField(
        blank=True,
        null=True
    )
    twitter= models.URLField(
        blank=True,
        null=True
    )
"""
