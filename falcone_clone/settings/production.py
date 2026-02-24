from .base import *
from decouple import config

DEBUG = config('DEBUG', default=False, cast=bool)
ENV = config('ENVIRONMENT', default='production')

ALLOWED_HOSTS = config(
    'ALLOWED_HOSTS',
    default='falconoptics.com.ua,www.falconoptics.com.ua,vps71960.hyperhost.name',
    cast=lambda v: [s.strip() for s in v.split(',') if s.strip()],
)

MEDIA_ROOT = '/var/www/media/'

# Cloudflare / reverse proxy
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
USE_X_FORWARDED_HOST = True


# Security
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
CSRF_TRUSTED_ORIGINS = [
    "https://falconoptics.com.ua",
    "https://www.falconoptics.com.ua",
]
