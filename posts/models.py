from django.db import models

# Create your models here.

#게시글에는 어떤 목록이 있을까?????제목 글쓴이 조회수
from django.db import models
from django.utils import timezone

class Post(models.Model):
    title = models.CharField(max_length=100)  #게시글제목
    content = models.TextField()              #게시글본문
    author = models.CharField(max_length=50)  #글쓴이
    views = models.PositiveIntegerField(default=0)  #조회수

    created_at = models.DateTimeField(default=timezone.now)  #작성시간
    updated_at = models.DateTimeField(auto_now=True)         #수정시간

    def __str__(self):
        return f"{self.title} by {self.author}"

    def increase_views(self):
        self.views += 1
        self.save()
