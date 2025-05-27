from django.urls import path   #각 유알엘 경로를 정의해주는 장고 함수 샤라웃
from .views import login_view, signup_view, logout_view, test #뷰에서 로그인, 회원가입, 로그아웃 함수 불러옴
from django.shortcuts import render #템플릿을 불러와서 html로 렌더링 

app_name = "users" #urls.py 안에 유저스라는 앱이 공식적인 멤버로 인정됨

def test(request): #테스트 함수로 브라우저에 보여짐
    return render(request, "test.html")


urlpatterns = [
    path("login/", login_view, name="login"), #/유저스/로그인/ 사용자 로그인 페이지
    path("signup/", signup_view, name="signup"), #유저스/사인업/ 회원가입 페이지
    path("logout/", logout_view, name="logout"), #유저스/로그아웃/ 로그아웃 페이지 
    path("test/", test, name="test"),  
]
