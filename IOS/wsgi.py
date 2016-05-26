"""
WSGI config for IOS project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

'''import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "IOS.settings")

application = get_wsgi_application()'''

import os
import sys

root = os.path.dirname(__file__)
sys.path.insert(0, os.path.join(root, '..', 'site-packages'))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "honey.settings")

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
