from django.urls import path
from instaAPP.views import (HelloWorld, PostsListView, PostDetailView, 
                    PostCreateView, PostUpdateView, PostDeleteView,
                    SignUp)

urlpatterns = [
    path('', HelloWorld.as_view(), name='home'),
    path('posts/', PostsListView.as_view(), name='posts'),
    #<> provide extra parameter, int type, pk primary key
    path('post/<int:pk>', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='make_post'), 
    path('post/edit/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('post/delete/<int:pk>', PostDeleteView.as_view(), name='post_delete'),
    path('auth/signup', SignUp.as_view(), name='signup'),
]