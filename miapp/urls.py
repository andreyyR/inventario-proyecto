from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('registro/', views.registro, name='registro'),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='inicio'), name='logout'),
    
    # URLs de Productos
    path('productos/', views.productos_lista, name='productos_lista'),
    path('productos/crear/', views.producto_crear, name='producto_crear'),
    path('productos/<int:id>/', views.producto_detalle, name='producto_detalle'),
    path('productos/editar/<int:id>/', views.producto_editar, name='producto_editar'),
    path('productos/eliminar/<int:id>/', views.producto_eliminar, name='producto_eliminar'),
    
    # URLs de Categorías
    path('categorias/', views.categorias_lista, name='categorias_lista'),
    path('categorias/crear/', views.categoria_crear, name='categoria_crear'),
    path('categorias/<int:id>/', views.categoria_detalle, name='categoria_detalle'),
    path('categorias/editar/<int:id>/', views.categoria_editar, name='categoria_editar'),
    path('categorias/eliminar/<int:id>/', views.categoria_eliminar, name='categoria_eliminar'),
    
    # URLs de Clientes
    path('clientes/', views.clientes_lista, name='clientes_lista'),
    path('clientes/crear/', views.cliente_crear, name='cliente_crear'),
    path('clientes/<int:id>/', views.cliente_detalle, name='cliente_detalle'),
    path('clientes/editar/<int:id>/', views.cliente_editar, name='cliente_editar'),
    path('clientes/eliminar/<int:id>/', views.cliente_eliminar, name='cliente_eliminar'),

    # URLs de Ventas
    path('ventas/', views.ventas_lista, name='ventas_lista'),
    path('ventas/crear/', views.venta_crear, name='venta_crear'),
    path('ventas/<int:id>/', views.venta_detalle, name='venta_detalle'),
] 