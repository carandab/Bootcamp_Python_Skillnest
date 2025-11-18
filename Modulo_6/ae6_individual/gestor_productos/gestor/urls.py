from django.urls import path
from django.contrib import admin
from .views import IndexView, LoginView, LogoutView, RegisterView, ProductoListView, ProductoAddView, ProductoUpdateView, ProductoDeleteView


urlpatterns = [

    # Vistas principales
    path('', IndexView.as_view(), name='index'),
    
    # Autenticación de Usuarios
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView, name='logout'),
    path('register/', RegisterView, name='register'),
    
    # CRUD
    path('productos/', ProductoListView.as_view(), name='productos'),
    path('productos/crear/', ProductoAddView.as_view(), name='crear_producto'),
    path('productos/editar/<int:pk>/', ProductoUpdateView.as_view(), name='editar_producto'),
    path('productos/borrar/<int:pk>/', ProductoDeleteView.as_view(), name='borrar_producto'),
]