from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  # 로그인 후 이동할 경로
            else:
                form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form})
