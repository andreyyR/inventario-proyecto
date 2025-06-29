"""
Configuración de Django para el proyecto `inventario_project`.

Este archivo define todas las configuraciones para la aplicación Django,
incluyendo la base de datos, aplicaciones instaladas, rutas de archivos estáticos,
y la configuración de seguridad y autenticación.
"""

import os
from pathlib import Path

# BASE_DIR: Define la ruta base del proyecto.
# Se utiliza para construir rutas relativas a otros archivos del proyecto.
BASE_DIR = Path(__file__).resolve().parent.parent


# Configuración de seguridad y desarrollo rápido
# En producción, estas configuraciones deben ser ajustadas por seguridad.

# SECRET_KEY: Clave secreta utilizada para la seguridad de Django.
# ¡Advertencia de seguridad! Mantener esta clave secreta en producción.
SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-9=^*^k30@==h*)hh#qui1d-jbdr*g11i4$*2c%0)_51pmdpr3!')

# DEBUG: Habilita/deshabilita el modo de depuración.
# True en desarrollo para ver errores detallados. ¡False en producción por seguridad!
DEBUG = os.environ.get('DEBUG', 'True').lower() == 'true'

# ALLOWED_HOSTS: Lista de nombres de host/IP que pueden servir esta aplicación Django.
# En producción, debe contener los dominios de tu sitio web.
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', 'localhost,127.0.0.1').split(',')


# Definición de aplicaciones
# INSTALLED_APPS: Lista de todas las aplicaciones Django activas en este proyecto.
# Incluye aplicaciones integradas de Django y nuestras aplicaciones personalizadas.
INSTALLED_APPS = [
    'django.contrib.admin',        # Interfaz de administración de Django
    'django.contrib.auth',         # Sistema de autenticación de usuarios
    'django.contrib.contenttypes', # Marcos para tipos de contenido
    'django.contrib.sessions',     # Gestión de sesiones de usuario
    'django.contrib.messages',     # Marco de mensajes
    'django.contrib.staticfiles',  # Gestión de archivos estáticos
    'whitenoise.runserver_nostatic',  # Para servir archivos estáticos en desarrollo
    'miapp',                       # Nuestra aplicación personalizada de inventario
]

# MIDDLEWARE: Lista de middleware a ejecutar en cada solicitud.
# El middleware es un marco de hooks de procesamiento ligero que se ejecuta en la fase de solicitud/respuesta de Django.
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',     # Seguridad básica
    'whitenoise.middleware.WhiteNoiseMiddleware',        # Para servir archivos estáticos
    'django.contrib.sessions.middleware.SessionMiddleware', # Habilita sesiones
    'django.middleware.common.CommonMiddleware',         # Configuración común de Django
    'django.middleware.csrf.CsrfViewMiddleware',         # Protección contra ataques CSRF
    'django.contrib.auth.middleware.AuthenticationMiddleware', # Habilita la autenticación de usuarios
    'django.contrib.messages.middleware.MessageMiddleware', # Habilita mensajes flash
    'django.middleware.clickjacking.XFrameOptionsMiddleware', # Protección Clickjacking
]

# ROOT_URLCONF: Especifica el módulo que contiene la configuración de URL raíz del proyecto.
ROOT_URLCONF = 'inventario_project.urls'

# TEMPLATES: Configuración de los motores de plantilla de Django.
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: Lista de directorios donde Django buscará archivos de plantilla.
        # Aquí se especifica que las plantillas de nuestra aplicación 'miapp' están en su propio subdirectorio 'templates'.
        'DIRS': [BASE_DIR / 'miapp' / 'templates'],
        'APP_DIRS': True, # Habilita la búsqueda de plantillas dentro de los directorios 'templates' de las aplicaciones instaladas.
        'OPTIONS': {
            # context_processors: Funciones que añaden variables al contexto de todas las plantillas.
            'context_processors': [
                'django.template.context_processors.request',   # Acceso al objeto request en las plantillas
                'django.contrib.auth.context_processors.auth',  # Acceso a user en las plantillas (autenticación)
                'django.contrib.messages.context_processors.messages', # Acceso a mensajes flash
            ],
        },
    },
]

# WSGI_APPLICATION: Especifica el objeto WSGI de la aplicación principal.
# Utilizado por servidores web para servir la aplicación Django.
WSGI_APPLICATION = 'inventario_project.wsgi.application'


# Configuración de la base de datos
# DATABASES: Define las configuraciones de la base de datos.
# Configurado para usar MySQL con variables de entorno para producción
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Motor de base de datos MySQL
        'NAME': os.environ.get('DB_NAME', 'inventario_db'),              # Nombre de la base de datos
        'USER': os.environ.get('DB_USER', 'root'),                       # Usuario de MySQL
        'PASSWORD': os.environ.get('DB_PASSWORD', 'Andrey0305#'),        # Contraseña del usuario
        'HOST': os.environ.get('DB_HOST', 'localhost'),                  # Host donde está MySQL
        'PORT': os.environ.get('DB_PORT', '3306'),                       # Puerto por defecto de MySQL
        'OPTIONS': {
            'charset': 'utf8mb4',             # Codificación de caracteres
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'", # Modo SQL estricto
        },
    }
}


# Validación de contraseñas
# AUTH_PASSWORD_VALIDATORS: Lista de validadores que se aplican a las contraseñas de los usuarios.
# Ayuda a reforzar la seguridad de las contraseñas.
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internacionalización
# Configuración relacionada con el idioma y la zona horaria.
LANGUAGE_CODE = 'en-us' # Código de idioma por defecto (ej. 'es-cr' para español de Costa Rica si se quiere más específico)

TIME_ZONE = 'UTC'      # Zona horaria del proyecto (se puede cambiar a 'America/Costa_Rica' si se desea)

USE_I18N = True        # Habilita el soporte para internacionalización (traducciones)

USE_TZ = True          # Habilita el soporte para zonas horarias


# Archivos estáticos (CSS, JavaScript, Imágenes)
# STATIC_URL: URL para referenciar archivos estáticos (usado en plantillas con {% static '...' %}).
STATIC_URL = '/static/'
# STATIC_ROOT: Directorio donde se recolectarán los archivos estáticos para producción
STATIC_ROOT = BASE_DIR / 'staticfiles'
# STATICFILES_DIRS: Lista de directorios adicionales donde Django buscará archivos estáticos.
# Aquí se incluye el directorio 'static' en la raíz del proyecto.
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
# Configuración de WhiteNoise para archivos estáticos
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# MEDIA_URL: URL para referenciar archivos de medios subidos por los usuarios (ej. imágenes de productos).
MEDIA_URL = '/media/'
# MEDIA_ROOT: Ruta absoluta al directorio donde se guardarán los archivos de medios subidos.
MEDIA_ROOT = BASE_DIR / 'media'

# Configuración de Login y Logout
# LOGIN_REDIRECT_URL: URL a la que se redirige después de un login exitoso.
LOGIN_REDIRECT_URL = 'inicio'
# LOGOUT_REDIRECT_URL: URL a la que se redirige después de un logout exitoso.
LOGOUT_REDIRECT_URL = 'inicio'
# LOGIN_URL: URL de la página de login.
LOGIN_URL = 'login'

# Configuración de Mensajes
# MESSAGE_TAGS: Mapea los niveles de mensajes de Django a clases CSS de Bootstrap.
# Permite estilizar los mensajes flash (éxito, error, etc.) de forma consistente.
from django.contrib.messages import constants as messages
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# DEFAULT_AUTO_FIELD: Tipo de campo para las claves primarias automáticas en los modelos.
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Configuración de seguridad para producción
if not DEBUG:
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = 'DENY'
    SECURE_HSTS_SECONDS = 31536000
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
