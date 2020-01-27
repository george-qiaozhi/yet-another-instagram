from annoying.decorators import ajax_request
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .forms import CustomUserCreationForm

from .models import Post, Like, UserConnection, InstaUser

# CRUD

class PostsListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "master_view.html"
    login_url = "login"

    def get_queryset(self):
        current_user = self.request.user
        following = set()
        for conn in UserConnection.objects.filter(creator=current_user).select_related('following'):
            following.add(conn.following)
        return Post.objects.filter(author__in=following)


class PostDetailView(LoginRequiredMixin, DetailView):
    model = Post
    template_name = "post_detail.html"
    #if not logged in, jump to login
    login_url = "login"


class PostCreateView(CreateView):
    model = Post
    template_name = "post_create.html"
    fields = '__all__'


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


# Profile
class UserDetailView(LoginRequiredMixin, DetailView):
    model = InstaUser
    template_name = "user_detail.html"
    login_url = "login"

# like, comment
@ajax_request  # non-class based, not belong to an object
def addLike(request):
    post_pk = request.POST.get('post_pk')
    post = Post.objects.get(pk=post_pk)
    try:
        like = Like(post=post, user=request.user)
        like.save() # <== this line might throw exception: Like.Meta.uniqueTogether
        result = 1
    except Exception as e:
        like = Like.objects.get(post=post, user=request.user)
        like.delete()
        result = 0

    return {
        'result': result,
        'post_pk': post_pk
    }