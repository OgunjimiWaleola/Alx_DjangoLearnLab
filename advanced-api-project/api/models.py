from django.db import models
from django.core.exceptions import ValidationError
from datetime import date

# Author model to store author information
class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# Book model to store book information
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        related_name='books'  # Allows reverse lookup: author.books.all()
    )

    def __str__(self):
        return self.title

    
    def clean(self):
        if self.publication_year > date.today().year:
            raise ValidationError('Publication year cannot be in the future.')
        
#Author model stores authors.

#Book model has a ForeignKey to Author, creating a one-to-many relationship.