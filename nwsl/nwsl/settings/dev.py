from .base import *
import json #noqa


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '48dfxp5x$af*$#qxbxymzylq40byvypqf1w1)c=sz_u=)$#df$'

ALLOWED_HOSTS = ['*']

BASE_DIR = '/var/wwww/nwsl'

INSTALLED_APPS += [
  'django_sass', 
  # Added sass compling. https://terencelucasyap.com/using-sass-django/
  'sass_processor', 
  
  ]
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'sass_processor.finders.CssFinder',
]

# Django Sass
SASS_PROCESSOR_ROOT = os.path.join(BASE_DIR,'static')

with open("/etc/nwsl.conf") as config_file:
  site_config = json.load(config_file)

SECRET_KEY = site_config['SECRETKEY']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

try:
    from .local_settings import *
except ImportError:
    pass
