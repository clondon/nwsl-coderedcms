"""
WSGI config for watfordwillsandtrusts project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/howto/deployment/wsgi/
"""

import os
import sys

from django.core.wsgi import get_wsgi_application


sys.path.append('/var/www/watfordwillsandtrusts')
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "watfordwillsandtrusts.settings.dev")

application = get_wsgi_application()
