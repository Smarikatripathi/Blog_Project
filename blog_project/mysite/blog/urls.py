from django.urls import path
from blog import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),  # URL for the post list view
    path('about/', views.AboutView.as_view(), name='about'),  # URL for the about page}
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),  # URL for post detail view
    path('post/new/', views.CreatePostView.as_view(), name='post_new'),  # URL for creating a new post
    path('post/<int:pk>/edit/', views.PostUpdateView.as_view(), name='post_edit'),  # URL for editing a post
    path('post/<int:pk>/remove/', views.PostDeleteView.as_view(), name='post_remove'),  # URL for deleting a post
    path('drafts/', views.DraftListView.as_view(), name='post_draft_list'),  # URL for draft list view
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),  # URL for adding a comment to a post
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),  # URL for approving a comment
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),  # URL for removing a comment
    path('post/<int:pk>/publish/', views.post_publish, name='post_publish'),  # URL for publishing a post



]
