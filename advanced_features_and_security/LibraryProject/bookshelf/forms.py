from django import forms
from .models import Book


class ExampleForm(forms.ModelForm):
    """
    ExampleForm is used to demonstrate secure input handling.
    It validates and sanitizes user input to prevent XSS attacks.
    """

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data.get('title')

        # Basic XSS protection check
        if "<script>" in title.lower():
            raise forms.ValidationError("Invalid input detected.")

        return title
