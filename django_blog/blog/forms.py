from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Post, Comment
from taggit.forms import TagWidget
from taggit.managers import TaggableManager



# User Registration Form

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Post Form with Tags

class PostForm(forms.ModelForm):
    # Optional: allow comma-separated tags input
    tags = forms.CharField(
        required=False, 
        help_text="Enter tags separated by commas"
    )

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # This integrates with django-taggit
        }

    def save(self, commit=True):
        instance = super().save(commit=False)

        if commit:
            instance.save()

        # Handle comma-separated tags manually if needed
        tag_names = self.cleaned_data.get("tags", "")
        for tag_name in tag_names.split(","):
            tag_name = tag_name.strip()
            if tag_name:
                instance.tags.add(tag_name)  # TaggableManager handles string names

        return instance


# Comment Form

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']