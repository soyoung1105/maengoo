from django import forms
from .models import User #사용자의 모델데이터 
from django.contrib.auth import get_user_model

User = get_user_model() #사용자 모델 가져오기

class LoginForm(forms.Form): #로그인 폼
    username = forms.CharField(label="아이디", max_length=150) #아이디 입력란
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput) #비번 입력란(숨김처리)


class SignupForm(forms.ModelForm): #회원가입 폼 
    username = forms.CharField(label="아이디", max_length=150) #아이디 입력란
    password = forms.CharField(widget=forms.PasswordInput, label="비밀번호")
    password2 = forms.CharField(widget=forms.PasswordInput, label="비밀번호 확인")
    
    class Meta:
        model = User #모델 데이터와 유저(사용자) 연결
        fields = ['username', 'password'] #유저 네임과 비번을 입력할 필드 
    #사인업내에서 클래스를 지정 (메타 데이터)) 사인업 폼 안에 데이터
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password2 = cleaned_data.get("password2")
        if password and password2 and password != password2:
            raise forms.ValidationError("비밀번호가 일치하지 않습니다.")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user