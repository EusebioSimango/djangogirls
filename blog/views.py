from django.shortcuts import render
from django.utils import timezone
from .models import Post
# Create your views here.


def post_list(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_info(request, title, author):
    post = Post.objects.filter(title=title).first()
    print(post.title)
    return render(request, 'blog/post_info.html', {'post': post})
