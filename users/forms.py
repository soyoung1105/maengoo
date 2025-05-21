from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label="아이디", max_length=150)
    password = forms.CharField(label="비밀번호", widget=forms.PasswordInput)
