#非同期処理に対応したWebアプリケーションを動作させるための、Python製Webサーバーです
"""
ASGI config for googlecalendarapp project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'googlecalendarapp.settings')

application = get_asgi_application()
