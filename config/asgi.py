"""
ASGI config for config project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application #장고의 ASGI 앱 불러옴

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") #어떤 설정 파일을 쓸지 지정

application = get_asgi_application() #서버가 장고를 실행할 수 있게 준비
