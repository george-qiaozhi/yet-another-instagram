from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
#from django.contrib.auth.forms import UserCreationForm
from instaAPP.forms import CustomUserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post

# CRUD
class HelloWorld(TemplateView):
    template_name = "home.html"

class PostsListView(ListView):
    model = Post
    template_name = "master_view.html"

class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    #if not logged in, jump to login
    login_url = 'login'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "post_create.html"
    fields = '__all__'
    login_url = 'login'

class PostUpdateView(UpdateView):
    model = Post
    template_name = "post_update.html"
    fields = ['title']

class PostDeleteView(DeleteView):
    model = Post
    template_name = "post_delete.html"
    # cannot delete & reverse at the same time, so delay reverse
    success_url = reverse_lazy("posts")


# USER
class SignUp(CreateView):
    #form_class = UserCreationForm
    form_class = CustomUserCreationForm
    template_name = 'signup.html'
    success_url = reverse_lazy("login")