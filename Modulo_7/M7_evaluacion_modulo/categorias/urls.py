from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_categorias, name='lista_categorias'),
    path('crear/', views.crear_categoria, name='crear_categoria'),
    path('<int:id>/editar/', views.editar_categoria, name='editar_categoria'),
    path('<int:id>/eliminar/', views.eliminar_categoria, name='eliminar_categoria'),
]