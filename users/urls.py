from django.urls import path   #각 유알엘 경로를 정의해주는 장고 함수 샤라웃
from .views import login_view #뷰.pyㅇ에서 로그인 뷰 함수를 불러옴
from django.shortcuts import render #템플릿을 불러와서 html로 렌더링 

app_name = "users" #urls.py 안에 유저스라는 앱이 공식적인 멤버로 인정됨

def test(request): #테스트용으로 브라우저에 보여짐
    return render(request, "test.html")
urlpatterns = [   
    path("test/", test, name="test"),  #브라우저 주소창에 /유저/테스트/ 로 들어오면 test.html 화면을 보여줌
    path('login/', login_view, name='login'), #주소창에 /users/login  치면 로그인 창이 나옴
]
