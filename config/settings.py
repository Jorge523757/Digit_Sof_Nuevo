"""
DIGIT SOFT - Sistema de Gestión Empresarial
Configuración Principal
"""

from pathlib import Path
import os
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent

# Cargar variables de entorno desde .env
load_dotenv(BASE_DIR / '.env')

SECRET_KEY = 'django-insecure-digt-soft-2024-cambiar-en-produccion'
DEBUG = True
ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    '0.0.0.0',
    '192.168.1.56',       # IP Ethernet
    '192.168.1.*',        # Red Ethernet completa
    '192.168.137.1',      # IP del adaptador de área local
    '192.168.137.221',    # IP WiFi
    '192.168.137.*',      # Toda la red WiFi
    '*',                  # Permite todas las conexiones (solo desarrollo)
]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # Requerido por allauth

    # Django Allauth (Login con Google)
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',

    # Apps del proyecto
    'main',  # App principal con modelos Cart y CartItem
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
    'reportes_dano',  # Sistema de reporte de daños
    'notificaciones',  # Sistema de notificaciones
    'ayuda',  # Sistema de ayuda y soporte
    'backups',  # Sistema de copias de seguridad
    'utils',  # Utilidades y filtros personalizados
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',  # Requerido por allauth
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

# Configuración de Base de Datos SQLite
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
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
# CONFIGURACIÓN DE EMAIL PARA NOTIFICACIONES
# ============================================================================

import os

# Backend de email - SMTP REAL para envío rápido de correos
EMAIL_BACKEND = os.getenv('EMAIL_BACKEND', 'django.core.mail.backends.smtp.EmailBackend')

# Configuración SMTP para Gmail optimizada para velocidad
EMAIL_HOST = os.getenv('EMAIL_HOST', 'smtp.gmail.com')
EMAIL_PORT = int(os.getenv('EMAIL_PORT', '587'))
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', 'True') == 'True'
EMAIL_USE_SSL = False  # TLS en puerto 587 es más rápido que SSL en 465

# Credenciales de Gmail
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')  # Tu email de Gmail
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')  # Contraseña de aplicación

# Email por defecto para envíos
DEFAULT_FROM_EMAIL = os.getenv('DEFAULT_FROM_EMAIL', f'DIGIT SOFT <{EMAIL_HOST_USER}>')

# Email del administrador para recibir notificaciones
ADMIN_EMAIL = os.getenv('ADMIN_EMAIL', EMAIL_HOST_USER)

# URL del sitio (para enlaces en emails)
SITE_URL = os.getenv('SITE_URL', 'http://localhost:8000')

# Configuraciones adicionales para optimizar velocidad de envío
EMAIL_TIMEOUT = 30  # Timeout de 30 segundos
EMAIL_SSL_CERTFILE = None
EMAIL_SSL_KEYFILE = None

# ⚠️ FORZAR SMTP REAL - NO cambiar a consola automáticamente
# Si las credenciales están vacías, el sistema mostrará el código en pantalla
# pero intentará enviar por SMTP de todas formas

# ============================================================================
# INSTRUCCIONES PARA CONFIGURAR GMAIL:
# ============================================================================
# 1. Ve a: https://myaccount.google.com/apppasswords
# 2. Activa la verificación en dos pasos
# 3. Genera una contraseña de aplicación para "Correo"
# 4. Copia la contraseña generada y úsala en EMAIL_HOST_PASSWORD
# ============================================================================

# ============================================================================
# CONFIGURACIÓN DE DJANGO-ALLAUTH (LOGIN CON GOOGLE)
# ============================================================================

SITE_ID = 1

# Configuración de autenticación
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  # Backend por defecto
    'allauth.account.auth_backends.AuthenticationBackend',  # Backend de allauth
]

# Configuración de allauth (actualizada para Django-allauth 6.x)
ACCOUNT_LOGIN_METHODS = {'email', 'username'}
ACCOUNT_SIGNUP_FIELDS = ['email*', 'username', 'password1*', 'password2*']
ACCOUNT_EMAIL_VERIFICATION = 'optional'  # Puedes cambiarlo a 'mandatory' si quieres

# Permitir vincular cuentas de Google a usuarios existentes con el mismo email
SOCIALACCOUNT_AUTO_SIGNUP = True
SOCIALACCOUNT_EMAIL_REQUIRED = True
SOCIALACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_UNIQUE_EMAIL = True

# Adaptadores personalizados
ACCOUNT_ADAPTER = 'usuarios.adapters.CustomAccountAdapter'
SOCIALACCOUNT_ADAPTER = 'usuarios.adapters.CustomSocialAccountAdapter'

# Redirecciones
SOCIALACCOUNT_LOGIN_ON_GET = True
LOGIN_REDIRECT_URL = 'dashboard:index'
ACCOUNT_LOGOUT_REDIRECT_URL = '/usuarios/login/'
LOGOUT_REDIRECT_URL = 'core:home'

# Configuración de Google OAuth
# NOTA: Las credenciales se manejan desde la base de datos (SocialApp model)
# No incluir 'APP' aquí porque causa MultipleObjectsReturned
SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

# ============================================================================
# INSTRUCCIONES PARA CONFIGURAR GOOGLE OAUTH:
# ============================================================================
# 1. Ve a: https://console.cloud.google.com/
# 2. Crea un proyecto nuevo o selecciona uno existente
# 3. Habilita "Google+ API"
# 4. Ve a "Credenciales" > "Crear credenciales" > "ID de cliente de OAuth 2.0"
# 5. Tipo de aplicación: "Aplicación web"
# 6. URIs de redirección autorizados:
#    - http://localhost:8000/accounts/google/login/callback/
#    - http://127.0.0.1:8000/accounts/google/login/callback/
# 7. Copia el Client ID y Client Secret
# 8. Pégalos arriba en SOCIALACCOUNT_PROVIDERS
# ============================================================================

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# Authentication
LOGIN_URL = 'usuarios:login'
LOGIN_REDIRECT_URL = 'dashboard:index'
LOGOUT_REDIRECT_URL = 'core:home'
