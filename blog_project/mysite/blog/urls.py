from django.conf.urls import path
from blog import views

urlpatterns = [
    path('', views.PostlistView.as_view(), name='post_list'),  # URL for the post list view
    path('about/', views.AboutView.as_view(), name='about'),  # URL for the about page}
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # URL for post detail view
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),  # URL for creating a new post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # URL for editing a post
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),  # URL for deleting a post

]
