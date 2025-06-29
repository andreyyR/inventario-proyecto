# miapp/models.py
# Este archivo define los modelos de datos para la aplicación de inventario.
# Cada clase de modelo representa una tabla en la base de datos y sus atributos son las columnas.

from django.db import models
from django.contrib.auth.models import User # Importa el modelo de usuario de Django para relaciones

# Modelo Categoria: Representa una categoría a la que pueden pertenecer los productos.
class Categoria(models.Model):
    nombre = models.CharField(max_length=100) # Nombre de la categoría (ej. 'Electrónica', 'Ropa')
    descripcion = models.TextField(blank=True) # Descripción opcional de la categoría
    creado_en = models.DateTimeField(auto_now_add=True) # Fecha y hora de creación (se establece automáticamente)

    # Método __str__: Define la representación de cadena del objeto.
    # Se utiliza en la interfaz de administración de Django y cuando se imprime un objeto Categoria.
    def __str__(self):
        return self.nombre

    # Clase Meta: Proporciona metadatos para el modelo.
    class Meta:
        verbose_name = 'Categoría' # Nombre singular legible para humanos
        verbose_name_plural = 'Categorías' # Nombre plural legible para humanos

# Modelo Producto: Representa un artículo individual en el inventario.
class Producto(models.Model):
    nombre = models.CharField(max_length=200) # Nombre del producto
    descripcion = models.TextField() # Descripción detallada del producto
    precio = models.DecimalField(max_digits=10, decimal_places=2) # Precio del producto con 2 decimales
    stock = models.IntegerField(default=0) # Cantidad de producto disponible en inventario
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE) # Clave foránea a Categoria (un producto pertenece a una categoría)
                                                                     # CASCADE: si la categoría se elimina, los productos asociados también se eliminan.
    imagen = models.ImageField(upload_to='productos/', null=True, blank=True) # Campo para subir imágenes de productos.
                                                                            # Las imágenes se guardarán en la carpeta 'media/productos/'.
    creado_en = models.DateTimeField(auto_now_add=True) # Fecha y hora de creación del producto
    actualizado_en = models.DateTimeField(auto_now=True) # Fecha y hora de la última actualización del producto

    # Método __str__: Representación de cadena del objeto Producto.
    def __str__(self):
        return self.nombre

    # Clase Meta: Metadatos para el modelo Producto.
    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'

# Modelo Cliente: Representa un cliente que realiza compras.
class Cliente(models.Model):
    nombre = models.CharField(max_length=200) # Nombre completo del cliente
    email = models.EmailField(unique=True) # Correo electrónico del cliente (debe ser único)
    telefono = models.CharField(max_length=20) # Número de teléfono del cliente
    direccion = models.TextField() # Dirección del cliente
    creado_en = models.DateTimeField(auto_now_add=True) # Fecha y hora de creación del registro del cliente

    # Método __str__: Representación de cadena del objeto Cliente.
    def __str__(self):
        return self.nombre

    # Clase Meta: Metadatos para el modelo Cliente.
    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'

# Modelo Venta: Representa una transacción de venta.
# Una venta registra qué cliente compró qué productos y por quién fue vendida.
class Venta(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE) # Clave foránea a Cliente (la venta pertenece a un cliente)
    fecha_venta = models.DateTimeField(auto_now_add=True) # Fecha y hora en que se realizó la venta
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE) # Clave foránea a User (el usuario que registró la venta)

    # Método get_total: Calcula el total de la venta sumando los subtotales de todos sus detalles de venta.
    # Este método itera sobre todos los objetos DetalleVenta relacionados con esta Venta (accediendo via 'detalles').
    def get_total(self):
        return sum(detalle.get_subtotal() for detalle in self.detalles.all()) # Suma de subtotales

    # Método __str__: Representación de cadena del objeto Venta.
    def __str__(self):
        return f"Venta {self.id} - {self.cliente.nombre} ({self.fecha_venta.strftime('%Y-%m-%d')})"

    # Clase Meta: Metadatos para el modelo Venta.
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        ordering = ['-fecha_venta'] # Ordena las ventas por fecha_venta de forma descendente (más recientes primero)

# Modelo DetalleVenta: Representa una línea de producto dentro de una Venta.
# Una Venta puede tener múltiples DetalleVenta, y cada DetalleVenta se refiere a un Producto específico.
class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE, related_name='detalles') # Clave foránea a Venta (el detalle pertenece a una venta).
                                                                                       # related_name='detalles' permite acceder a los detalles desde una Venta (ej. venta.detalles.all()).
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE) # Clave foránea a Producto (el detalle se refiere a un producto específico).
    cantidad = models.IntegerField() # Cantidad del producto vendido en esta línea.
    precio_unitario = models.DecimalField(max_digits=10, decimal_places=2) # Precio del producto al momento de la venta.

    # Método save: Se sobrescribe para manejar la lógica antes de guardar el objeto.
    # Aquí se asegura que el precio unitario se tome del producto si no se especifica, y se actualiza el stock.
    def save(self, *args, **kwargs):
        # Si el precio_unitario no está establecido, toma el precio actual del producto.
        if not self.precio_unitario:
            self.precio_unitario = self.producto.precio
        super().save(*args, **kwargs) # Llama al método save original para guardar el objeto.
        # Actualiza el stock del producto: resta la cantidad vendida del stock actual.
        self.producto.stock -= self.cantidad
        self.producto.save() # Guarda el producto con el stock actualizado.

    # Método get_subtotal: Calcula el subtotal de esta línea de venta.
    def get_subtotal(self):
        return self.cantidad * self.precio_unitario

    # Método __str__: Representación de cadena del objeto DetalleVenta.
    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre} en Venta {self.venta.id}"

    # Clase Meta: Metadatos para el modelo DetalleVenta.
    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalles de Venta'
        # unique_together: Asegura que un producto solo puede aparecer una vez por venta.
        unique_together = ('venta', 'producto') 