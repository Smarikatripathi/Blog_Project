from django import forms
from blog.models import Post, comment

class PostForm(forms.ModelForm): # Form for creating and editing posts
    class Meta:
        model = Post
        fields = ('author','title', 'text')

        widgets = {
            'title': forms.Textarea(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'}),


        }         

class commentForm(forms.ModelForm): # Form for creating and editing comments
    class Meta:
        model = comment
        fields = ('author', 'text') # Fields to include in the form  

        widgets = {
            'author': forms.TextInput(attrs={'class':'textinputclass'}),
            'text': forms.Textarea(attrs={'class':'editable medium-editor-textarea '}),

        }             
