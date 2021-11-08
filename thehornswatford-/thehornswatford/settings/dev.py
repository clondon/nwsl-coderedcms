from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '_3j-0#3y%4*0wej0qspoi^!^obc0d-eu!i@ni63w#iu_%oq_)3'

ALLOWED_HOSTS = ['thehornswatford.co.uk','www.thehornswatford.co.uk','18.170.95.92','localhost','127.0.0.1',]

INSTALLED_APPS =  INSTALLED_APPS + ['django_sass', 'debug_toolbar']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

WAGTAIL_CACHE = False

MIDDLEWARE = MIDDLEWARE  + [   
    'debug_toolbar.middleware.DebugToolbarMiddleware',  
]

INTERAL_IPS = ('127.0.0.1','172.26.10.187','18.170.95.92')

try:
    from .local_settings import *
except ImportError:
    pass
