from django.urls import path
from . import views

urlpatterns = [
    path('recetas/', views.lista_recetas, name='lista_recetas'),
]