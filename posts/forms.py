from django import forms
from .models import Post

#게시글작성/수정 시 사용함
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'author']
