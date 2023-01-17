#本番環境等にデプロイする際にサーバーの設定を行います
"""
WSGI config for googlecalendarapp project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'googlecalendarapp.settings')

application = get_wsgi_application()
