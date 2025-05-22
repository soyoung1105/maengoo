from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="아이디", max_length=150) #아이디 입력란
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput) #비번 입력란(숨김처리)
