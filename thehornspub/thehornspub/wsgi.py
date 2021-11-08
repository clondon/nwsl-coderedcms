"""
WSGI config for the Horns Pub project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os 
import sys





sys.path.append('/var/www/.thehornspub_env')
sys.path.append('/var/www/thehornspub')
sys.path.append('/var/www/thehornspub/thehornspub')

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "thehornspub.settings.dev")
# os.environ["DJANGO_SETTINGS_MODULE"] = "{{ thehornspub }}.dev"
application = get_wsgi_application()
