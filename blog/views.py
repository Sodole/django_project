from django.shortcuts import render
from .models import Post
# Create views.

def index(request) :
    posts = Post.objects.all().order_by('-pk')

    return render(request, 'blog/index.html',{'posts':posts,})
