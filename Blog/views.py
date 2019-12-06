from django.shortcuts import render , redirect ,get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin , UserPassesTestMixin
from .models import Blog
from django.contrib.auth.models import User
from django.core.paginator import Paginator

from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
    )

class BlogListView(ListView):
    template_name = 'blog_home.html'
    model = Blog
    context_object_name = 'posts'
    ordering = ['-date_posted']
    paginate_by = 4

# class UserPostListView(ListView):
#     template_name = 'user_post.html'
#     model = Blog
#     context_object_name = 'posts'
#     paginate_by = 2
    
#     def get_query_set(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return Blog.objects.filter(authors=user).order_by('-date_posted')

class BlogDetailView(DetailView):
    template_name = 'blog_detail.html'
    model = Blog

class BlogCreateView(LoginRequiredMixin , CreateView):
    template_name = 'blog_create.html'
    model = Blog 
    fields = ['title' , 'description']  

    def form_valid(self, form):
        form.instance.authors = self.request.user 
        return super().form_valid(form) 

class BlogUpdateView(LoginRequiredMixin ,UserPassesTestMixin, UpdateView):
    template_name = 'blog_create.html'
    model = Blog 
    fields = ['title' , 'description']  

    def form_valid(self, form):
        form.instance.authors = self.request.user 
        return super().form_valid(form)    

    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.authors:
            return True
        return False  

class BlogDeleteView(LoginRequiredMixin ,UserPassesTestMixin, DeleteView):
    template_name = 'blog_delete.html'
    model = Blog
    success_url = '/'
    def test_func(self):
        blog = self.get_object()
        if self.request.user == blog.authors:
            return True
        return False       

def About(request):
    return render(request , "blog_about.html" , {'title' : 'contact'})