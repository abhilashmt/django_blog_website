from django.shortcuts import render

# Create your views here.
posts = [
    {
        'title': 'Blog 1',
        'author': 'Adam Gilchrist',
        'date': '20 August, 2019',
        'content': 'This is my first blog'
    }, {
        'title': 'Blog 2',
        'author': 'Sachin Tendulkar',
        'date': '20 July, 2019',
        'content': 'This is my second blog'
    }
]
title = {
    'home_title': 'Home',
    'about_title': 'About'
}


def home(request):
    context = {
        'posts': posts,
        'title': title
    }
    return render(request, 'blog/home.html', context)


def about(request):
    context = {
        'title': title
    }
    return render(request, 'blog/about.html', context)
