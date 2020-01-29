"""instaAPP URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from instaAPP.views import (PostsListView, PostDetailView, ExploreView,
                    PostCreateView, MakeInstaPost, PostUpdateView, PostDeleteView,
                    addLike, addComment, toggleFollow, 
                    SignUp, UserDetailView, UserUpdateView,
                    FollowerProfile, FollowingProfile)

urlpatterns = [
    path('', PostsListView.as_view(), name='home'),
    #<> provide extra parameter, int type, pk primary key
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', MakeInstaPost.as_view(), name='make_post'), 
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('auth/signup', SignUp.as_view(), name='signup'),
    path('like', addLike, name='addLike'),
    path('comment', addComment, name='addComment'),
    path('togglefollow', toggleFollow, name='togglefollow'),
    path('user/<int:pk>', UserDetailView.as_view(), name='user_detail'),
    path('user/edit/<int:pk>', UserUpdateView.as_view(), name='user_update'),
    path('explore', ExploreView.as_view(), name='explore'),
    path('follower/<int:pk>/', FollowerProfile.as_view(), name='follower'),
    path('following/<int:pk>/', FollowingProfile.as_view(), name='following'),
]