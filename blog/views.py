from django.shortcuts import render
from django.http import HttpResponse
from .models import Post


#dummy data for understanding templates and views
'''
posts = [
    {
        'author':'Akash',
        'title':'Blog Post 1',
        'content':'First Blog Content',
        'post_posted':'17 March 2001',
    },
    {
        'author':'Soumya',
        'title':'Blog Post 2',
        'content':'Second Blog Content',
        'post_posted':'14 January 1979',
    },
]'''


def homePage(request):
    context = {
        'posts': Post.objects.all() 
    }
    
    return render(request,'blog/index.html',context)

def aboutPage(request):
    return render(request,'blog/about.html',{'title':'About'})
