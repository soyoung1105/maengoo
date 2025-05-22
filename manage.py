#!/usr/bin/env python #파이썬으로 시작하겠다
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main(): #설정파일지정
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
    try:
        from django.core.management import execute_from_command_line #명령어
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv) #터미널 명령어 실행


if __name__ == "__main__":
    main() #메인함수 실행
