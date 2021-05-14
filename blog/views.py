from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView
)
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


class PostListView(ListView):
    model = Post
    template_name = 'blog/index.html'
    context_object_name = 'posts'
    ordering = ['-post_posted']


class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False

         
    
    

def aboutPage(request):
    return render(request,'blog/about.html',{'title':'About'})
