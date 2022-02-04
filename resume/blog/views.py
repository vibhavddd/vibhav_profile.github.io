from django.shortcuts import render
from .models import Blog

def all_blog(requests):
    blogs = Blog.objects.order_by('-date')
    context= {
        'blogs':blogs
    }
    return render(requests, 'blog/all_blog.html',context)