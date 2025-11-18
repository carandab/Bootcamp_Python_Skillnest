from django.contrib import admin 
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #Panel de administración de Django
    path('admin/', admin.site.urls),

    #URLs Públicas - Sin autenticación necesaria
    # Incluir apps con namespace para poder usar {% url 'app_eventos:...' %} y {% url 'auth:...' %}
    path('', include(('app_eventos.urls', 'app_eventos'), namespace='app_eventos')),

    #URLs Privadas - Requieren autenticación
    path('', include(('login.urls', 'auth'), namespace='auth')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
