from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('formulario1/', views.registrar_evento, name='formulario1'),
    path('formulario2/', views.registrar_persona, name='formulario2'),
]