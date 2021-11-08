from .base import *
import mimetypes
import json #noqa
import os #noqa

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
ALLOWED_HOSTS = ['127,0,0,1','18.170.95.92']

# SECURITY WARNING: keep the secret key used in production secret!

with open("/etc/nwsl.conf") as config_file:
  site_config = json.load(config_file)

SECRET_KEY = site_config['SECRETKEY']
# Add your site's domain name(s) here.
ALLOWED_HOSTS = ['www.new-web-sites.com','new-web-sites.com','18.170.95.92']



INSTALLED_APPS += ['django_sass','debug_toolbar',]
MIDDELWARE = MIDDLEWARE + [ 'debug_toolbar.middleware.DebugToolbarMiddleware',]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
