"""
Configuración de URL para el proyecto `inventario_project`.

Este archivo define las rutas URL principales de la aplicación.
Las `urlpatterns` enlazan las URLs con las vistas de Django.

Para más información, consulta:
https://docs.djangoproject.com/en/5.2/topics/http/urls/
"""
from django.contrib import admin # Importa el módulo de administración de Django
from django.urls import path, include # Importa funciones para definir rutas URL
from django.conf import settings # Importa la configuración del proyecto
from django.conf.urls.static import static # Importa funciones para servir archivos estáticos/media en desarrollo

# urlpatterns: Lista de todas las rutas URL del proyecto.
# Django procesa estas rutas en orden para encontrar una coincidencia para la URL solicitada.
urlpatterns = [
    # Ruta raíz: Incluye las URLs definidas en la aplicación 'miapp'.
    # Esto significa que las rutas de 'miapp/urls.py' se manejarán desde la URL raíz del proyecto.
    path('', include('miapp.urls')),
    
    # Ruta de administración: Define la URL para el panel de administración de Django.
    path('admin/', admin.site.urls),
] 

# Configuración para servir archivos de medios (imágenes, videos, etc.) en modo de desarrollo.
# Solo se utiliza cuando DEBUG es True. En producción, los servidores web (como Nginx o Apache) manejan esto.
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
