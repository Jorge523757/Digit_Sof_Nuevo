"""
DIGIT SOFT - Sistema de Gestión Empresarial
Configuración Principal
"""

from pathlib import Path
import os
import environ

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env
env = environ.Env()
environ.Env.read_env(BASE_DIR / '.env')

SECRET_KEY = 'django-insecure-digt-soft-2024-cambiar-en-produccion'
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '192.168.1.56',
    '192.168.1.*',
    '192.168.137.1',
    '192.168.137.221',
    '192.168.137.*',
    '*',
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    # Django Allauth (Login con Google)
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Apps del proyecto
    'main',
    'core',
    'usuarios',
    'dashboard',
    'clientes',
    'tecnicos',
    'ordenes',
    'proveedores',
    'productos',
    'garantias',
    'compras',
    'ventas',
    'facturacion',
    'equipos',
    'capacitaciones',
    'reportes_dano',
    'notificaciones',
    'ayuda',
    'backups',
    'utils',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'

# Configuración de Base de Datos MySQL
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': env('DB_NAME', default='digitsoft'),
        'USER': env('DB_USER', default='root'),
        'PASSWORD': env('DB_PASSWORD', default=''),
        'HOST': env('DB_HOST', default='localhost'),
        'PORT': env('DB_PORT', default='3306'),
    }
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'usuarios.validators.ValidadorSimilitudAtributos',
        'OPTIONS': {
            'user_attributes': ('username', 'email', 'first_name', 'last_name'),
            'max_similarity': 0.7,
        }
    },
    {
        'NAME': 'usuarios.validators.ValidadorLongitudMinima',
        'OPTIONS': {
            'min_length': 8,
        }
    },
    {
        'NAME': 'usuarios.validators.ValidadorContrasenaComun',
    },
    {
        'NAME': 'usuarios.validators.ValidadorContrasenaNumerica',
    },
]

LANGUAGE_CODE = 'es-es'
TIME_ZONE = 'America/Mexico_City'
USE_I18N = True

# ============================================================================
# CONFIGURACIÓN DE EMAIL
# ============================================================================

EMAIL_BACKEND = env('EMAIL_BACKEND', default='django.core.mail.backends.smtp.EmailBackend')
EMAIL_HOST = env('EMAIL_HOST', default='smtp.gmail.com')
EMAIL_PORT = int(env('EMAIL_PORT', default='587'))
EMAIL_USE_TLS = env('EMAIL_USE_TLS', default='True') == 'True'
EMAIL_USE_SSL = False
EMAIL_HOST_USER = env('EMAIL_HOST_USER', default='')
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD', default='')
DEFAULT_FROM_EMAIL = env('DEFAULT_FROM_EMAIL', default=f'DIGIT SOFT <{EMAIL_HOST_USER}>')
ADMIN_EMAIL = env('ADMIN_EMAIL', default=EMAIL_HOST_USER)
SITE_URL = env('SITE_URL', default='http://localhost:8000')
EMAIL_TIMEOUT = 30
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None

# ============================================================================
# CONFIGURACIÓN DE DJANGO-ALLAUTH (LOGIN CON GOOGLE)
# ============================================================================

SITE_ID = 1

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_LOGIN_METHODS = {'email', 'username'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = 'optional'

SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_UNIQUE_EMAIL = True

ACCOUNT_ADAPTER = 'usuarios.adapters.CustomAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'usuarios.adapters.CustomSocialAccountAdapter'

SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = 'dashboard:index'
ACCOUNT_LOGOUT_REDIRECT_URL = '/usuarios/login/'
LOGOUT_REDIRECT_URL = 'core:home'

# Credenciales Google OAuth desde .env
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'APP': {
            'client_id': env('GOOGLE_CLIENT_ID', default=''),
            'secret': env('GOOGLE_CLIENT_SECRET', default=''),
            'key': ''
        },
        'SCOPE': ['profile', 'email'],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# ============================================================================
# ARCHIVOS ESTÁTICOS Y MEDIA
# ============================================================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

LOGIN_URL = 'usuarios:login'
LOGIN_REDIRECT_URL = 'dashboard:index'
LOGOUT_REDIRECT_URL = 'core:home'