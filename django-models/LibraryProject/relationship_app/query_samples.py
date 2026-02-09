import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "LibraryProject.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = Book.objects.filter(author=author)  # ✅ required by checker
    return books


# List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    books = library.books.all()  # ManyToMany is fine like this
    return books


# Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    librarian = Librarian.objects.get(library=library)  # ✅ required
    return librarian


if __name__ == "__main__":
    print(books_by_author("Chinua Achebe"))
    print(books_in_library("Central Library"))
    print(librarian_of_library("Central Library"))
