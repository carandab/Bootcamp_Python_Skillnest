from django.contrib import admin
from .models import Estudiantes, Profesores, Cursos, Inscripciones, Perfiles


class InscripcionesInline(admin.TabularInline):
    model = Inscripciones

@admin.register(Profesores)
class ProfesoresAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email')
    search_fields = ('nombre', 'email')

@admin.register(Cursos)
class CursosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'profesor', 'descripcion')
    search_fields = ('id', 'nombre', 'profesor')
    inlines = [InscripcionesInline]

@admin.register(Estudiantes)
class EstudiantesAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'email')
    search_fields = ('nombre', 'email')
    inlines = [InscripcionesInline]

@admin.register(Inscripciones)  
class InscripcionesAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'curso', 'fecha_inscripcion', 'estado', 'nota_final')
    search_fields = ('id', 'estudiante', 'curso', 'estado')

class EstudiantesInline(admin.TabularInline):
    model = Estudiantes

@admin.register(Perfiles)
class PerfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'estudiante', 'biografia', 'foto', 'redes')
    search_fields = ('id', 'estudiante')
    inlines = [EstudiantesInline]

