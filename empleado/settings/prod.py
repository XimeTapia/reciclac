from .base import *

DEBUG = False

ROOT_URLCONF = 'empleado.urls'

ALLOWED_HOSTS = [
    'reciclac-1.onrender.com',
    '.onrender.com',
]

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
