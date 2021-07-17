from django.urls import path
from feed.views import (PostListView, FollowsListView, FollowersListView)
from feed import views

urlpatterns = [
    path('', PostListView.as_view(), name='home'),
    path('most-liked/', views.global_feed, name='global'),
    path('search_posts/', views.search_posts, name='search_posts'),
    path('upload/', views.create_post, name='upload-video'),
    path('user/<str:username>/follows',FollowsListView.as_view(),name='user-follows'),
    path('user/<str:username>/followers',FollowersListView.as_view(),name='user-followers'),
]