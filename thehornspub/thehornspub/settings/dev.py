from .base import *  # noqa

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

import json

# Open the config file
with open("/etc/thehorns_pub.conf") as config_file:
  site_config = json.load(config_file)



# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = site_config['SECRETKEY'] 

ALLOWED_HOSTS = ['18.170.95.92:8000','18.170.95.92','thehornswatford.co.uk','www.thehornswatford.co.uk']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False


if DEBUG:
    import mimetypes
    mimetypes.add_type("image/png", ".png", True)
    mimetypes.add_type("image/jpg", ".jpg", True)
    INSTALLED_APPS = INSTALLED_APPS + ['django_sass', ]

try:
    from .local_settings import *  # noqa
except ImportError:
    pass
