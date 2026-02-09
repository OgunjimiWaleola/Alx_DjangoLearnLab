import os
import django

# Setup Django environment
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_models.settings")
django.setup()

from relationship_app.models import Author, Book, Library, Librarian


# -------------------------
# Sample Queries
# -------------------------

# 1️⃣ Query all books by a specific author
def books_by_author(author_name):
    author = Author.objects.get(name=author_name)
    books = author.books.all()
    return books


# 2️⃣ List all books in a library
def books_in_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.books.all()


# 3️⃣ Retrieve the librarian for a library
def librarian_of_library(library_name):
    library = Library.objects.get(name=library_name)
    return library.librarian


# -------------------------
# Example test run
# -------------------------
if __name__ == "__main__":
    print("Books by Chinua Achebe:")
    print(books_by_author("Chinua Achebe"))

    print("\nBooks in Central Library:")
    print(books_in_library("Central Library"))

    print("\nLibrarian of Central Library:")
    print(librarian_of_library("Central Library"))
