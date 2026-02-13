from django import forms
from .models import Book

class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'published_date']

    def clean_title(self):
        title = self.cleaned_data['title']
        if "<script>" in title:
            raise forms.ValidationError("Invalid input detected!")
        return title
