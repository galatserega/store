# falcone_clone/settings/local.py
import os
from .base import *
from decouple import config

# Local development settings

DEBUG = config('DEBUG', default=True, cast=bool)
ENV = config('ENVIRONMENT', default='development')
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='localhost,127.0.0.1', cast=lambda v: [s.strip() for s in v.split(',')])
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
# Папка зі статичними файлами в проекті
STATICFILES_DIRS = [os.path.join(BASE_DIR, '..', 'static')]
# Куди збирати статичні файли командою collectstatic
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, '..', 'media')
