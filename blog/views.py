from django.shortcuts import render
from django.http import HttpResponse



#dummy data for understanding templates and views

posts = [
    {
        'author':'Akash',
        'title':'Blog Post 1',
        'content':'First Blog Content',
        'data_publish':'17 March 2001',
    },
    {
        'author':'Soumya',
        'title':'Blog Post 2',
        'content':'Second Blog Content',
        'data_publish':'14 January 1979',
    },
]
def homePage(request):
    context = {

        'posts': posts 
    }
    
    return render(request,'blog/index.html',context)

def aboutPage(request):
    return render(request,'blog/about.html',{'title':'About'})
