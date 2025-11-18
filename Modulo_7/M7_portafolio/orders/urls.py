from django.urls import path
from . import views

app_name = 'orders'

urlpatterns = [
    path('checkout/', views.checkout, name='checkout'),
    path('mis-pedidos/', views.order_list, name='lista_pedidos'),
    path('pedidos/<int:pk>/', views.order_detail, name='detalle_pedido'),
]