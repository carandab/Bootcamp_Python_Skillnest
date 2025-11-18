from django.urls import path
from . import views

app_name = 'gestor'

urlpatterns = [
    # Voluntarios
    path('voluntarios/', views.lista_voluntarios, name='lista_voluntarios'),
    path('voluntarios/crear/', views.crear_voluntario, name='crear_voluntario'),
    path('voluntarios/<int:pk>/', views.detalle_voluntario, name='detalle_voluntario'),
    path('voluntarios/<int:pk>/actualizar/', views.actualizar_voluntario, name='actualizar_voluntario'),
    path('voluntarios/<int:pk>/eliminar/', views.confirmar_eliminar_voluntario, name='confirmar_eliminar_voluntario'),
    
    # Eventos
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/<int:pk>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/<int:pk>/actualizar/', views.actualizar_evento, name='actualizar_evento'),
    path('eventos/<int:pk>/eliminar/', views.confirmar_eliminar_evento, name='confirmar_eliminar_evento'),
]