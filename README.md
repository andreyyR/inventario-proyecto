# Sistema de Inventario - Django

Un sistema completo de gestión de inventario desarrollado con Django y MySQL.

## 🚀 Características

- **Gestión de Productos**: CRUD completo con imágenes
- **Categorías**: Organización de productos
- **Clientes**: Gestión de información de clientes
- **Ventas**: Sistema de ventas con múltiples productos
- **Control de Stock**: Actualización automática
- **Panel de Administración**: Interfaz completa de Django Admin
- **Autenticación**: Sistema de usuarios y permisos
- **Responsive Design**: Bootstrap 5 para móviles y desktop

## 🛠️ Tecnologías

- **Backend**: Django 5.2.3
- **Base de Datos**: MySQL
- **Frontend**: Bootstrap 5, HTML5, CSS3
- **JavaScript**: Vanilla JS para funcionalidades dinámicas
- **Servidor**: Gunicorn (producción)

## 📋 Requisitos

- Python 3.12+
- MySQL 8.0+
- WAMP/XAMPP (para desarrollo local)

## 🔧 Instalación

### 1. Clonar el repositorio
```bash
git clone <tu-repositorio>
cd inventario_project
```

### 2. Crear entorno virtual
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

### 3. Instalar dependencias
```bash
pip install -r requirements.txt
```

### 4. Configurar base de datos
- Crear base de datos MySQL: `inventario_db`
- Configurar variables de entorno o editar `settings.py`

### 5. Ejecutar migraciones
```bash
python manage.py migrate
```

### 6. Crear superusuario
```bash
python manage.py createsuperuser
```

### 7. Ejecutar servidor
```bash
python manage.py runserver
```

## 🌐 Acceso

- **Aplicación**: http://localhost:8000
- **Admin**: http://localhost:8000/admin

## 📁 Estructura del Proyecto

```
inventario_project/
├── inventario_project/     # Configuración principal
├── miapp/                  # Aplicación principal
│   ├── models.py          # Modelos de datos
│   ├── views.py           # Vistas y lógica
│   ├── forms.py           # Formularios
│   ├── admin.py           # Panel de administración
│   └── templates/         # Plantillas HTML
├── static/                # Archivos estáticos
├── media/                 # Archivos subidos
├── requirements.txt       # Dependencias
└── manage.py             # Script de gestión
```

## 🔐 Variables de Entorno

Para producción, configurar estas variables:

```env
SECRET_KEY=tu-clave-secreta
DEBUG=False
ALLOWED_HOSTS=tu-dominio.com
DB_NAME=inventario_db
DB_USER=tu-usuario
DB_PASSWORD=tu-contraseña
DB_HOST=tu-host
DB_PORT=3306
```

## 🚀 Deployment

### Railway (Recomendado)
1. Conectar repositorio GitHub
2. Configurar variables de entorno
3. Deploy automático

### Heroku
1. Crear aplicación Heroku
2. Configurar PostgreSQL
3. Deploy con Git

## 📝 Uso

### Usuarios Administradores
- Acceso completo a todas las funcionalidades
- Gestión de productos, categorías, clientes y ventas
- Panel de administración

### Usuarios Regulares
- Visualización de productos y categorías
- Acceso limitado a funcionalidades

## 🤝 Contribución

1. Fork el proyecto
2. Crear rama feature (`git checkout -b feature/AmazingFeature`)
3. Commit cambios (`git commit -m 'Add AmazingFeature'`)
4. Push a la rama (`git push origin feature/AmazingFeature`)
5. Abrir Pull Request

## 📄 Licencia

Este proyecto está bajo la Licencia MIT.

## 👥 Autores

- Tu Nombre - Desarrollo inicial

## 🙏 Agradecimientos

- Django Framework
- Bootstrap
- MySQL Community 