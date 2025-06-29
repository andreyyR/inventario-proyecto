INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'miapp',  # Nuestra aplicación
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'inventario_db',     # Nombre de la base de datos que crearemos
        'USER': 'andreyrr',              # Usuario de MySQL (por defecto es 'root')
        'PASSWORD': 'Andrey0305',              # Contraseña de tu usuario de MySQL
        'HOST': 'localhost',         # Host donde está MySQL (normalmente localhost)
        'PORT': '3307',              # Puerto por defecto de MySQL
    }
}

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'miapp' / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

STATIC_URL = 'static/'
STATICFILES_DIRS = [
    BASE_DIR / 'miapp' / 'static',
] 