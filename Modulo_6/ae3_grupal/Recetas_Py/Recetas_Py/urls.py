"""
URL configuration for Recetas_Py project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from . import views  
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.inicio, name='inicio'),  # Página de inicio
    path('recetas/', views.lista_recetas, name='lista_recetas'),  # Página de recetas
    path('contacto/', views.contacto, name='contacto'),  # Página de contacto
    path('recetas/<int:receta_id>/', views.detalle_receta, name='detalle_receta'),
    path('', include('recetas.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
