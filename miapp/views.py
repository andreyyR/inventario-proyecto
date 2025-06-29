# miapp/views.py
# Este archivo contiene las vistas (funciones) de la aplicación de inventario.
# Cada vista procesa una solicitud HTTP y devuelve una respuesta, típicamente renderizando una plantilla HTML.

from django.shortcuts import render, redirect, get_object_or_404 # Importa funciones de atajo para renderizar, redirigir y obtener objetos
from django.contrib.auth.decorators import login_required, user_passes_test # Decoradores para restringir el acceso a vistas
from django.contrib.auth import login, authenticate # Funciones para manejar el login y la autenticación de usuarios
from django.contrib.auth.forms import UserCreationForm # Formulario de Django para la creación de usuarios
from django.contrib import messages # Framework de mensajes para notificaciones al usuario
from django.forms import inlineformset_factory # Utilidad para manejar conjuntos de formularios relacionados (formsets)

# Importa los modelos y formularios definidos en la misma aplicación
from .models import Producto, Categoria, Cliente, Venta, DetalleVenta
from .forms import ProductoForm, CategoriaForm, ClienteForm, VentaForm, DetalleVentaForm

# Función auxiliar para verificar si un usuario es administrador (staff).
# Utilizada con el decorador @user_passes_test.
def es_admin(user):
    return user.is_staff

# Vista para el registro de nuevos usuarios.
def registro(request):
    # Si la solicitud es POST (se envió el formulario de registro)
    if request.method == 'POST':
        form = UserCreationForm(request.POST) # Crea una instancia del formulario con los datos enviados
        # Si el formulario es válido (los datos cumplen las reglas de validación)
        if form.is_valid():
            user = form.save() # Guarda el nuevo usuario en la base de datos
            login(request, user) # Inicia sesión al usuario recién registrado
            messages.success(request, '¡Registro exitoso!') # Muestra un mensaje de éxito
            return redirect('inicio') # Redirige a la página de inicio
    # Si la solicitud es GET (primera vez que se accede al formulario)
    else:
        form = UserCreationForm() # Crea una instancia de formulario vacío
    # Renderiza la plantilla de registro con el formulario
    return render(request, 'registro.html', {'form': form})

# Vista para la página de inicio del sistema.
@login_required # Requiere que el usuario esté autenticado para acceder
def inicio(request):
    # Obtiene los 5 productos más recientes para mostrar en la página de inicio
    productos = Producto.objects.all()[:5]
    # Obtiene todas las categorías
    categorias = Categoria.objects.all()
    # Renderiza la plantilla de inicio, pasando los productos y categorías al contexto
    return render(request, 'inicio.html', {
        'productos': productos,
        'categorias': categorias
    })

# CRUD para Productos
# Vista para listar todos los productos.
@login_required # Requiere que el usuario esté autenticado
def productos_lista(request):
    productos = Producto.objects.all() # Obtiene todos los productos de la base de datos
    return render(request, 'productos/lista.html', {'productos': productos}) # Renderiza la plantilla con los productos

# Vista para crear un nuevo producto.
@login_required # Requiere que el usuario esté autenticado
@user_passes_test(es_admin) # Solo usuarios administradores pueden acceder a esta vista
def producto_crear(request):
    # Si la solicitud es POST (se envió el formulario)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES) # Crea una instancia del formulario con datos POST y archivos
        if form.is_valid():
            form.save() # Guarda el nuevo producto en la base de datos
            messages.success(request, 'Producto creado exitosamente') # Muestra un mensaje de éxito
            return redirect('productos_lista') # Redirige a la lista de productos
    # Si la solicitud es GET
    else:
        form = ProductoForm() # Crea un formulario de producto vacío
    # Renderiza la plantilla de creación de producto con el formulario
    return render(request, 'productos/crear.html', {'form': form})

# Vista para ver los detalles de un producto específico.
@login_required # Requiere que el usuario esté autenticado
def producto_detalle(request, id):
    # Obtiene un producto por su ID; si no existe, devuelve un error 404
    producto = get_object_or_404(Producto, id=id)
    return render(request, 'productos/detalle.html', {'producto': producto}) # Renderiza la plantilla con los detalles del producto

# Vista para editar un producto existente.
@login_required # Requiere que el usuario esté autenticado
@user_passes_test(es_admin) # Solo usuarios administradores pueden acceder a esta vista
def producto_editar(request, id):
    # Obtiene el producto a editar por su ID
    producto = get_object_or_404(Producto, id=id)
    # Si la solicitud es POST
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto) # Crea un formulario con datos, archivos y la instancia del producto
        if form.is_valid():
            form.save() # Guarda los cambios en el producto
            messages.success(request, 'Producto actualizado exitosamente')
            return redirect('productos_lista')
    # Si la solicitud es GET
    else:
        form = ProductoForm(instance=producto) # Crea un formulario pre-llenado con los datos del producto existente
    # Renderiza la plantilla de edición con el formulario y el producto
    return render(request, 'productos/editar.html', {'form': form, 'producto': producto})

# Vista para eliminar un producto existente.
@login_required # Requiere que el usuario esté autenticado
@user_passes_test(es_admin) # Solo usuarios administradores pueden acceder a esta vista
def producto_eliminar(request, id):
    # Obtiene el producto a eliminar por su ID
    producto = get_object_or_404(Producto, id=id)
    producto.delete() # Elimina el producto de la base de datos
    messages.success(request, 'Producto eliminado exitosamente')
    return redirect('productos_lista')

# CRUD para Categorías
# Vista para listar todas las categorías.
@login_required # Requiere que el usuario esté autenticado
def categorias_lista(request):
    categorias = Categoria.objects.all() # Obtiene todas las categorías
    return render(request, 'categorias/lista.html', {'categorias': categorias}) # Renderiza la plantilla con las categorías

# Vista para crear una nueva categoría.
@login_required
@user_passes_test(es_admin) # Solo administradores
def categoria_crear(request):
    if request.method == 'POST':
        form = CategoriaForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría creada exitosamente')
            return redirect('categorias_lista')
    else:
        form = CategoriaForm()
    return render(request, 'categorias/crear.html', {'form': form})

# Vista para ver los detalles de una categoría específica.
@login_required
def categoria_detalle(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    return render(request, 'categorias/detalle.html', {'categoria': categoria})

# Vista para editar una categoría existente.
@login_required
@user_passes_test(es_admin) # Solo administradores
def categoria_editar(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria)
        if form.is_valid():
            form.save()
            messages.success(request, 'Categoría actualizada exitosamente')
            return redirect('categorias_lista')
    else:
        form = CategoriaForm(instance=categoria)
    return render(request, 'categorias/editar.html', {'form': form, 'categoria': categoria})

# Vista para eliminar una categoría existente.
@login_required
@user_passes_test(es_admin) # Solo administradores
def categoria_eliminar(request, id):
    categoria = get_object_or_404(Categoria, id=id)
    categoria.delete()
    messages.success(request, 'Categoría eliminada exitosamente')
    return redirect('categorias_lista')

# CRUD para Clientes
# Vista para listar todos los clientes.
@login_required
@user_passes_test(es_admin) # Solo administradores pueden ver la lista de clientes
def clientes_lista(request):
    clientes = Cliente.objects.all()
    return render(request, 'clientes/lista.html', {'clientes': clientes})

# Vista para crear un nuevo cliente.
@login_required
@user_passes_test(es_admin) # Solo administradores pueden crear clientes
def cliente_crear(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente creado exitosamente')
            return redirect('clientes_lista')
    else:
        form = ClienteForm()
    return render(request, 'clientes/crear.html', {'form': form})

# Vista para ver los detalles de un cliente específico.
@login_required
@user_passes_test(es_admin) # Solo administradores pueden ver el detalle del cliente
def cliente_detalle(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    return render(request, 'clientes/detalle.html', {'cliente': cliente})

# Vista para editar un cliente existente.
@login_required
@user_passes_test(es_admin) # Solo administradores pueden editar clientes
def cliente_editar(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            messages.success(request, 'Cliente actualizado exitosamente')
            return redirect('clientes_lista')
    else:
        form = ClienteForm(instance=cliente)
    return render(request, 'clientes/editar.html', {'form': form, 'cliente': cliente})

# Vista para eliminar un cliente existente.
@login_required
@user_passes_test(es_admin) # Solo administradores pueden eliminar clientes
def cliente_eliminar(request, id):
    cliente = get_object_or_404(Cliente, id=id)
    cliente.delete()
    messages.success(request, 'Cliente eliminado exitosamente')
    return redirect('clientes_lista')

# CRUD para Ventas
# Vista para crear una nueva venta.
@login_required
@user_passes_test(es_admin) # Solo administradores pueden crear ventas
def venta_crear(request):
    # Crea un formset para manejar múltiples detalles de venta asociados a una Venta.
    # inlineformset_factory: Crea una clase FormSet que puede manejar modelos relacionados.
    # Venta: Modelo padre; DetalleVenta: Modelo hijo; form: Formulario para el modelo hijo; extra: formularios vacíos por defecto.
    DetalleVentaFormSet = inlineformset_factory(Venta, DetalleVenta, form=DetalleVentaForm, extra=1, can_delete=True)

    # Si la solicitud es POST (se envió el formulario de venta)
    if request.method == 'POST':
        form = VentaForm(request.POST) # Instancia el formulario principal de Venta con los datos POST
        # Si el formulario de Venta es válido
        if form.is_valid():
            venta = form.save(commit=False) # Guarda la instancia de Venta pero no la persiste en la DB aún
            venta.vendedor = request.user # Asigna el usuario actual como el vendedor
            venta.save()  # Ahora sí, guarda la instancia de Venta en la base de datos

            # Instancia el formset de DetalleVenta con los datos POST y asocia los detalles a la venta recién creada.
            formset = DetalleVentaFormSet(request.POST, instance=venta)
            # Si el formset de detalles es válido
            if formset.is_valid():
                formset.save() # Guarda todos los DetalleVenta asociados a la Venta
                messages.success(request, 'Venta creada exitosamente') # Muestra mensaje de éxito
                return redirect('ventas_lista') # Redirige a la lista de ventas
            else:
                # Si el formset no es válido, se elimina la Venta principal para evitar registros huérfanos.
                venta.delete()
                messages.error(request, 'Error al guardar los detalles de la venta. Revise las cantidades y productos.')
                # Los errores específicos del formset se mostrarán en la plantilla.
        else:
            # Si el formulario principal de Venta no es válido, se vuelve a instanciar el formset
            # con los datos POST para que los errores se muestren y los datos ingresados no se pierdan.
            formset = DetalleVentaFormSet(request.POST)
            messages.error(request, 'Error al guardar la venta. Revise la información general.')
    # Si la solicitud es GET (primera vez que se accede al formulario)
    else:
        form = VentaForm() # Crea un formulario de Venta vacío
        formset = DetalleVentaFormSet(instance=None) # Crea un formset de DetalleVenta vacío (para una nueva venta)

    # Prepara el contexto para la plantilla y la renderiza
    context = {
        'form': form,
        'formset': formset,
    }
    return render(request, 'ventas/crear.html', context)

# Vista para listar todas las ventas.
@login_required
@user_passes_test(es_admin) # Solo administradores pueden ver la lista de ventas
def ventas_lista(request):
    ventas = Venta.objects.all().order_by('-fecha_venta') # Obtiene todas las ventas, ordenadas por fecha descendente
    return render(request, 'ventas/lista.html', {'ventas': ventas}) # Renderiza la plantilla con la lista de ventas

# Vista para ver los detalles de una venta específica.
@login_required
@user_passes_test(es_admin) # Solo administradores pueden ver el detalle de una venta
def venta_detalle(request, id):
    venta = get_object_or_404(Venta, id=id) # Obtiene la venta por su ID o devuelve 404
    detalles = venta.detalles.all() # Accede a todos los objetos DetalleVenta relacionados con esta venta
    return render(request, 'ventas/detalle.html', {'venta': venta, 'detalles': detalles}) # Renderiza la plantilla con los detalles de la venta

