from django import forms

class LoginForm(forms.Form): #로그인 폼
    username = forms.CharField(label="아이디", max_length=150) #아이디 입력란
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput) #비번 입력란(숨김처리)

from django import forms #장고의 폼 기능을 사용
from .models import User #사용자의 모델데이터 

class SignupForm(forms.ModelForm): #회원가입 폼 
    password = forms.CharField(widget=forms.PasswordInput) #비번 입력시숨김처리

    class Meta:
        model = User #모델 데이터와 유저(사용자) 연결
        fields = ['username', 'password'] #유저 네임과 비번을 입력할 필드 
