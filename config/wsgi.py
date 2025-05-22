"""
WSGI config for config project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os #os기능을 사용하기 위한 기본 모듈

from django.core.wsgi import get_wsgi_application #장고의 wsgi_application을 가져옴

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings") #환경 변수 설정

application = get_wsgi_application() #어플리케이션은 곧 wsgi_application이다
