from .base import *
import json #noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '48dfxp5x$af*$#qxbxymzylq40byvypqf1w1)c=sz_u=)$#df$'

ALLOWED_HOSTS = ['*']

INSTALLED_APPS += ['django_sass',]

with open("/etc/nwsl.conf") as config_file:
  site_config = json.load(config_file)

SECRET_KEY = site_config['SECRETKEY']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
