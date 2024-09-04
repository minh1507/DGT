"""
WSGI config for RA project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.core.management import call_command

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'DGT.settings')

if os.getenv("SOURCE_MIGRATION") == "true":
    call_command('makemigrations')
    call_command('migrate')

application = get_wsgi_application()