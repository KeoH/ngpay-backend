from .base import *
import os

DEBUG = True

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ng_pay',
        'USER': 'ng_pay',
        'PASSWORD': 'ngpay',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

STATIC_ROOT = os.path.join(BASE_DIR, '../../static')
MEDIA_ROOT = os.path.join(BASE_DIR, '../../media')

# CORS
# CORS_ORIGIN_ALLOW_ALL = True

CORS_ORIGIN_WHITELIST = (
    'localhost:8000',
    'localhost:8080',
    'localhost:4200',
    '127.0.0.1:9000'
)
