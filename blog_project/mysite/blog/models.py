from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.ForeignKey('auth.User',on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
        default=timezone.now())
    published_date = models.DateTimeField(
        blank=True, null=True)
    
    def publish(self): # Method to publish the post
        self.published_date = timezone.now() # Set the published date to now
        self.save()

    def approve_comments(self):
        return self.comments.filter(approved_comment=True) # Method to approve comments  
    
    def get_absolute_url(self): # Method to get the absolute URL of the comment
        return reverse("post_detail", kwargs={"pk": self.pk}) 

    def _str__(self):
        return self.title # String representation of the Post object


    class comment(models.Model):
        post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
        author = models.CharField(max_length=200)
        text = models.TextField()
        created_date = models.DateTimeField(
            default=timezone.now())
        approved_comment = models.BooleanField(default=False)

        def approve(self): # Method to approve the comment
            self.approved_comment = True
            self.save()

        def get_absolute_url(self):
            return reverse("post_list")
        
            

        def _str_(self):
            return self.text
            
             



