from django.urls import path
from .views import login_view
from django.shortcuts import render

app_name = "users"

def test(request):
    return render(request, "test.html")

urlpatterns = [
    path("test/", test, name="test"),
    path('login/', login_view, name='login'),
]
