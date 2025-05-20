from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# 사용자 모델을 정의.
# Django의 AbstractBaseUser와 PermissionsMixin을 상속.
# AbstractBaseUser는 기본적인 사용자 모델을 제공하고, PermissionsMixin은 권한 관련 기능을 추가.
class UserManager(BaseUserManager):
    # 일반 사용자 생성 메서드
    def create_user(self, username, password=None):
        # usernmae이 없으면 예외 발생
        if not username:
            raise ValueError("사용자 이름은 필수입니다.")
        # username >> user 객체 생성
        user = self.model(username=username)
        # 비밀번호 해시화 처리(암호화)
        user.set_password(password)
        # 사용자 데이터베이스에 저장
        user.save(using=self._db)
        # 생성된 사용자 반환
        return user
    
    # 관리자(superuser) 생성 메서드
    def create_superuser(self, username, password=None):
        # 관리자 username, password 생성
        user = self.create_user(username, password)
        # staff 권한 부여
        user.is_staff = True
        # superuser 권한 부여
        user.is_superuser = True
        # 관리자 데이터베이스에 저장
        user.save(using=self._db)
        # 생성된 관리자 반환
        return user

# 사용자 모델(테이블) 정의
# AbstractBaseUser와 PermissionsMixin을 상속받아 사용자 모델을 정의
class User(AbstractBaseUser, PermissionsMixin):
    # 사용자 이름 필드
    username = models.CharField(max_length=150, unique=True)
    # 비밀번호 필드
    password = models.CharField(max_length=128)
    # staff 필드
    is_staff = models.BooleanField(default=False)  # 관리자인지 여부

    # UserManager 객체 생성
    objects = UserManager()

    # 사용자 이름 필드
    USERNAME_FIELD = 'username'
    # createsuperuser 시 요구할 필드
    REQUIRED_FIELDS = []
    # 사용자 모델의 문자열 표현
    def __str__(self):
        return self.username