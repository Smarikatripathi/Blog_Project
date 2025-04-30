from django.shortcuts import render,get_object_or_404,redirect
from blog.models import Post, comment
from blog.forms import PostForm, commentForm
from django.urls import reverse_lazy
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import (TemplateView,ListView, DetailView, CreateView, UpdateView, DeleteView)
# Create your views here.

class AboutView(TemplateView):
    template_name = 'about.html'  # Path to your about.html template

class PostlistView(ListView):
    model = Post
    
    def get_queryset(self):
        return Post.objects.filter(published_date__lte=timezone.now().order_by('-published_date'))
    
class PostDetailView(DetailView):
    model = Post     

class CreatePostView(LoginRequiredMixin,CreateView):
    login_url = '/login/'  # Redirect to login page if not authenticated
    redirect_field_name = 'blog/post_detail.html'  # Redirect to this page after successful login

    from_class = PostForm  # Form for creating a new post
    model = Post # Create a new post ,connect to model Post
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    login_url = '/login/'  # Redirect to login page if not authenticated
    redirect_field_name = 'blog/post_detail.html'  # Redirect to this page after successful login

    form_class = PostForm  # Form for editing a post
    model = Post  # Connect to the Post model    
      
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post  # Connect to the Post model
    success_url = reverse_lazy('post_list')  # Redirect to the post list page after deletion      

class DraftListView(LoginRequiredMixin,ListView):
    login_url = '/login/'  # Redirect to login page if not authenticated
    redirect_field_name = 'blog/post_list.html'  # Redirect to this page after successful login

    model = Post  # Connect to the Post model

    def get_queryset(self):
        return Post.objects.filter(published_date__isnull=True).order_by('created_date')  # Filter for drafts only    
    
#######################################
@login_required
def post_publish(request,pk): # Publish a post
    post = get_object_or_404(Post, pk=pk) # Get the post object or return a 404 error if not found
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def add_comment_to_post(request,pk):
    post = get_object_or_404(Post, pk=pk)  # Get the post object or return a 404 error if not found
    if request.method == 'POST':
        form = commentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)  # Create a comment object but don't save it to the database yet
            comment.post = post  # Associate the comment with the post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = commentForm()
    return render(request, 'blog/comment_form.html', {'form': form})    
@login_required
def comment_approve(request,pk):
    comment = get_object_or_404(comment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

login_required
def comment_remove(request,pk):
    comment = get_object_or_404(comment, pk=pk)
    post_pk = comment.post.pk  # Store the post's primary key before deleting the comment
    comment.delete()  # Delete the comment
    return redirect('post_detail', pk=post_pk)  # Redirect to the post detail page after deletion




