from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('miapp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




urlpatterns = [
    # Productos
    path('productos/', views.productos_lista, name='productos_lista'),
    path('productos/crear/', views.producto_crear, name='producto_crear'),
    path('productos/<int:id>/editar/', views.producto_editar, name='producto_editar'),
    path('productos/<int:id>/eliminar/', views.producto_eliminar, name='producto_eliminar'),

    # Categorías
    path('categorias/', views.categorias_lista, name='categorias_lista'),
    path('categorias/crear/', views.categoria_crear, name='categoria_crear'),

    # Clientes
    path('clientes/', views.clientes_lista, name='clientes_lista'),
    path('clientes/crear/', views.cliente_crear, name='cliente_crear'),
]