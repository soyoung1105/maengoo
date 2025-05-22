from django.apps import AppConfig


class UsersConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField" #기본아이디 필드 타입
    name = "users" #앱 이름
