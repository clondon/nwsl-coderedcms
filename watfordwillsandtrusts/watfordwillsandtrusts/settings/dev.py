from .base import *
import mimetypes
import json


mimetypes.init() 
mimetypes.types_map['.css'] = 'text/css'
mimetypes.add_type("image/png", ".png", True)
mimetypes.add_type("image/jpg", ".jpg", True)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True 

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '-g3)2t=@l-+qe(sveugyivx1wci2sh_fka0mt*5huz1!n**1@f'

# Open the config file
with open("/etc/watfordwills.conf") as config_file:
  site_config = json.load(config_file)

SECRET_KEY = site_config['SECRETKEY'] 

ALLOWED_HOSTS = ['www.watfordwillsandtrusts.co.uk','watfordwillsandtrusts.co.uk','18.170.95.92']

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False


# Custom items.

if DEBUG:
    INSTALLED_APPS += ['django_sass','debug_toolbar', ]
    # INSTALLED_APPS = INSTALLED_APPS + ['django_sass', ]

    MIDDLEWARE += [ 'debug_toolbar.middleware.DebugToolbarMiddleware',]
    COMPRESS_PRECOMPILERS = (('text/x-scss', 'django_libsass.SassCompiler'),)

try:
    from .local_settings import *
except ImportError:
    pass
