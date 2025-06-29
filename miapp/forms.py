# miapp/forms.py
# Este archivo define los formularios utilizados en la aplicación de inventario.
# Los formularios de Django (ModelForms) facilitan la interacción con los modelos de la base de datos,
# validando datos y manejando la creación/actualización de objetos.

from django import forms
# Importa todos los modelos de la aplicación miapp que se utilizarán en los formularios.
from .models import Producto, Categoria, Cliente, Venta, DetalleVenta

# Formulario para el modelo Producto.
# Permite crear y editar instancias de Producto.
class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto # Asocia este formulario con el modelo Producto.
        # fields: Lista de campos del modelo que se incluirán en el formulario.
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'categoria', 'imagen']
        # widgets: Permite personalizar la apariencia de los campos HTML renderizados.
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}), # Hace el campo de descripción un área de texto con 3 filas.
            'precio': forms.NumberInput(attrs={'step': '0.01'}), # Define el paso para números decimales.
            'stock': forms.NumberInput(attrs={'min': '0'}), # Establece un valor mínimo de 0 para el stock.
        }

# Formulario para el modelo Categoria.
# Permite crear y editar instancias de Categoria.
class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria # Asocia este formulario con el modelo Categoria.
        fields = ['nombre', 'descripcion'] # Campos a incluir.
        widgets = {
            'descripcion': forms.Textarea(attrs={'rows': 3}), # Área de texto con 3 filas para la descripción.
        }

# Formulario para el modelo Cliente.
# Permite crear y editar instancias de Cliente.
class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente # Asocia este formulario con el modelo Cliente.
        fields = ['nombre', 'email', 'telefono', 'direccion'] # Campos a incluir.
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 3}), # Área de texto con 3 filas para la dirección.
        }

# Formulario para el modelo Venta.
# Utilizado para capturar la información general de una venta, como el cliente.
class VentaForm(forms.ModelForm):
    class Meta:
        model = Venta # Asocia este formulario con el modelo Venta.
        fields = ['cliente'] # Solo se incluye el campo cliente en este formulario principal.

# Formulario para el modelo DetalleVenta.
# Utilizado en un formset para añadir múltiples productos a una sola venta.
class DetalleVentaForm(forms.ModelForm):
    class Meta:
        model = DetalleVenta # Asocia este formulario con el modelo DetalleVenta.
        fields = ['producto', 'cantidad', 'precio_unitario'] # Campos a incluir para cada línea de producto en la venta.
        widgets = {
            'cantidad': forms.NumberInput(attrs={'min': '1'}), # Cantidad mínima de 1.
            'precio_unitario': forms.NumberInput(attrs={'step': '0.01'}), # Paso para números decimales en el precio unitario.
        } 