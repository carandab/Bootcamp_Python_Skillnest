from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'app_eventos'

urlpatterns = [
    #Path para la vista de inicio
    path('', views.inicio, name='inicio'),
    
    #Gestión de eventos
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    # Detalle de un evento individual
    path('eventos/<int:evento_id>/', views.detalle_evento, name='detalle_evento'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/editar/<int:evento_id>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:evento_id>/', views.eliminar_evento, name='eliminar_evento'),
    path('eventos/<int:evento_id>/registrar/', views.registrar_evento, name='registrar_evento'),
    path('eventos/<int:evento_id>/cancelar/', views.cancelar_registro_evento, name='cancelar_registro_evento'),
]
