from django.contrib import admin
from django.urls import path, include

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('producto.urls')),  
    path('categorias/', include('categorias.urls')),
    path('etiquetas/', include('etiquetas.urls')),
    
]