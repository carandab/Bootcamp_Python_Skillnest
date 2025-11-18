from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_etiquetas, name='lista_etiquetas'),
    path('crear/', views.crear_etiqueta, name='crear_etiqueta'),
    path('<int:id>/editar/', views.editar_etiqueta, name='editar_etiqueta'),
    path('<int:id>/eliminar/', views.eliminar_etiqueta, name='eliminar_etiqueta'),
]