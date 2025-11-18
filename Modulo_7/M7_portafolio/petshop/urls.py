from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from orders import views
from products import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    path('pedidos/', include('orders.urls')),
    path('usuarios/', include('users.urls')),
    
    # Carrito

    path('carrito/', views.cart_view, name='cart_view'),
    path('carrito/crear/<int:pk>/', views.add_to_cart, name='add_to_cart'),
    path('carrito/eliminar/<int:pk>/', views.remove_from_cart, name='remove_from_cart'),
    path('carrito/editar/<int:pk>/', views.update_cart, name='update_cart'),

]


# Servir archivos estáticos y de medios en desarrollo

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)