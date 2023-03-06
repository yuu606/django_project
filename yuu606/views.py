from django.shortcuts import render
from django.http import HttpResponse

posts = [
    {
    'author': 'yuu', 
    'title': 'Blog Post 1', 
    'content': 'First post content', 
    'date_posted': 'March 23, 2023'
    }, 
    {
    'author': 'Jane Doe', 
    'title': 'Blog Post 2', 
    'content': 'First post content', 
    'date_posted': 'March 24, 2023'
    }
]

def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})