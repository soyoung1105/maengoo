from django import forms
from .models import User #사용자의 모델데이터 

class LoginForm(forms.Form): #로그인 폼
    username = forms.CharField(label="아이디", max_length=150) #아이디 입력란
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput) #비번 입력란(숨김처리)


class SignupForm(forms.ModelForm): #회원가입 폼 
    password = forms.CharField(widget=forms.PasswordInput) #비번 입력시숨김처리

    class Meta:
        model = User #모델 데이터와 유저(사용자) 연결
        fields = ['username', 'password'] #유저 네임과 비번을 입력할 필드 
    #사인업내에서 클래스를 지정 (메타 데이터)) 사인업 폼 안에 데이터
    