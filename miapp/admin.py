# miapp/admin.py
# Este archivo configura cómo se muestran los modelos de la aplicación 'miapp' en la interfaz de administración de Django.

from django.contrib import admin # Importa el módulo de administración de Django
# Importa todos los modelos de la aplicación miapp para registrarlos en el admin.
from .models import Producto, Categoria, Cliente, Venta, DetalleVenta

# Registra el modelo Categoria en el panel de administración y personaliza su visualización.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    # list_display: Campos a mostrar en la lista de categorías en el admin.
    list_display = ('nombre', 'descripcion', 'creado_en')
    # search_fields: Campos por los que se puede buscar en la lista de categorías.
    search_fields = ('nombre',)

# Registra el modelo Producto en el panel de administración y personaliza su visualización.
@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    # list_display: Campos a mostrar en la lista de productos.
    list_display = ('nombre', 'categoria', 'precio', 'stock', 'creado_en')
    # list_filter: Permite filtrar la lista de productos por categoría.
    list_filter = ('categoria',)
    # search_fields: Campos por los que se puede buscar en la lista de productos.
    search_fields = ('nombre', 'descripcion')
    # list_editable: Campos que se pueden editar directamente desde la lista de productos.
    list_editable = ('precio', 'stock')

# Registra el modelo Cliente en el panel de administración y personaliza su visualización.
@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    # list_display: Campos a mostrar en la lista de clientes.
    list_display = ('nombre', 'email', 'telefono', 'creado_en')
    # search_fields: Campos por los que se puede buscar en la lista de clientes.
    search_fields = ('nombre', 'email')

# DetalleVentaInline: Permite editar los DetalleVenta directamente desde la página de Venta en el admin.
# admin.TabularInline: Muestra los formularios de DetalleVenta en formato tabular (tabla).
class DetalleVentaInline(admin.TabularInline):
    model = DetalleVenta # Modelo asociado a este inline.
    extra = 1  # Número de formularios vacíos adicionales a mostrar para añadir nuevos detalles.
    raw_id_fields = ('producto',) # Muestra un campo de búsqueda en lugar de un select para productos (útil para muchos productos).

# Registra el modelo Venta en el panel de administración y personaliza su visualización.
@admin.register(Venta)
class VentaAdmin(admin.ModelAdmin):
    # list_display: Campos a mostrar en la lista de ventas, incluyendo el total calculado.
    list_display = ('id', 'cliente', 'fecha_venta', 'get_total', 'vendedor')
    # list_filter: Permite filtrar la lista de ventas por fecha, vendedor o cliente.
    list_filter = ('fecha_venta', 'vendedor', 'cliente')
    # search_fields: Campos por los que se puede buscar en la lista de ventas.
    search_fields = ('cliente__nombre', 'vendedor__username')
    # inlines: Incluye DetalleVentaInline en la página de edición de Venta.
    inlines = [DetalleVentaInline]
    # date_hierarchy: Añade una navegación jerárquica por fechas en la parte superior de la lista de ventas.
    date_hierarchy = 'fecha_venta'

    # get_total: Método para calcular el total de la venta en la lista del admin.
    # Este método suma los subtotales de todos los detalles de venta asociados a la venta actual.
    def get_total(self, obj):
        return sum(detalle.get_subtotal() for detalle in obj.detalles.all())
    get_total.short_description = 'Total de Venta' # Etiqueta para la columna en list_display
