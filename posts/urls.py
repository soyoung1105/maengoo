#주소등록


from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),  #게시글목록
    path('post/<int:pk>/', views.post_detail, name='post_detail'),  #게시글상세
    path('post/new/', views.post_create, name='post_create'),  #게시글쓰기
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),  #게시글수정
    path('post/<int:pk>/delete/', views.post_delete, name='post_delete'),  #게시글삭제
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

