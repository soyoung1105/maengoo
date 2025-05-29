#주소등록

from django.urls import path
from . import views

app_name = 'posts'  #앱네임을 설정해줘야 템플릿에서 쓸 수 있음

urlpatterns = [
    path('', views.post_list, name='post_list'),  #홈가면 글 목록 뜨게
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  #글 눌렀을 때 디테일 보기
    path('post/new/', views.post_create, name='post_create'),  #새 글 쓰기 
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  #글 수정하는 곳
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),  #글 삭제할 때 여기씀
]




#        ╭┈┈┈┈╯           ╰┈┈┈╮

#         ╰┳┳╯             ╰┳┳╯
#        💧     　            💧

#        💧     　            💧
#                 ╰┈┈╯
#        💧      ╭━━━━━╮     💧
#                 ┈┈┈┈
#　      💧     　    　       💧 

# .　　　　\　　　|
# 　╲　　　　　　　　　　　╱
# 　　　　　\　　　　/
# 　　　╲　　　　　　　╱
# 　　╲　　 정말 　　　╱
# -　-　 고맙습니다 　  -　-
# 　　╱　　　　　　　　╲
# 　　╱　　/
# 　　╱　　　　　\　　╲
# 　　　　　/　|　　\
# 　　　　 　　|

