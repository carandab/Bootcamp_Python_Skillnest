from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/', views.product_list, name='lista_productos'),
    path('productos/<int:pk>/', views.product_detail, name='detalle_producto'),
    path('productos/crear/', views.product_create, name='crear_producto'),
    path('productos/editar/<int:pk>/', views.product_edit, name='editar_producto'),
    path('productos/eliminar/<int:pk>/', views.product_confirm_delete, name='confirmar_eliminar_producto'),
    path('carrito/', views.cart_view, name='cart_view'),
    path('carrito/agregar/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('carrito/agregar-cantidad/<int:pk>/', views.add_to_cart_with_quantity, name='add_to_cart_with_quantity'),
    path('carrito/eliminar/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('carrito/actualizar/<int:pk>/', views.update_cart, name='update_cart'),
]