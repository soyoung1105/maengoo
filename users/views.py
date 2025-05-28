from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect #화면 출력, 페이지 이동
from django.contrib.auth import authenticate, login , logout # 로그인 기능
from .forms import LoginForm , SignupForm #로그인 창 불러오기

def login_view(request):
    if request.method == 'POST': #폼 제출시 
        form = LoginForm(request.POST)
        if form.is_valid(): #유효성 검사 통과시
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password) #사용자 인증
            if user is not None:
                login(request, user)
                return redirect('post_list')  # 로그인 후 이동할 경로 (로그인 성공시 테스트페이지로)
            else:
                form.add_error(None, '아이디 또는 비밀번호가 올바르지 않습니다.') #로그인 실패시 에러 표시
    else:
        form = LoginForm() #겟 요청시 속이 빈 폼 생성..
    return render(request, 'users/login.html', {'form': form}) #로그인 페이지 재실행


from django.contrib.auth import login, logout

def signup_view(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])  # 비밀번호 암호화
            user.save()
            return redirect('users:login')  # 가입 후 로그인 페이지로 이동
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('post_list')  # 로그아웃 후 로그인 페이지로 이동

from django.shortcuts import render

def test(request):
    return render(request, 'test.html')  # 또는 간단한 텍스트 리턴도 가능
