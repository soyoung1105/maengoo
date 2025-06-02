from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from .forms import PostForm

#게시글목록보기
def post_list(request):
    posts = Post.objects.all().order_by('-created_at')  #정렬을 최신화
    return render(request, 'posts/post_list.html', {'posts': posts})

#게시글상세보기
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.increase_views()  #조회수증가
    return render(request, 'posts/post_detail.html', {'post': post})

#게시글작성
def post_create(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('posts:post_list')  #게시글 작성 후 목록으로 돌아가기
    else:
        form = PostForm()
    return render(request, 'posts/post_form.html', {'form': form})

#게시글수정
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts:post_detail', pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'posts/post_form.html', {'form': form})

#게시글 삭제
def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        post.delete()
        return redirect('posts:post_list')
    return render(request, 'posts/post_confirm_delete.html', {'post': post})
