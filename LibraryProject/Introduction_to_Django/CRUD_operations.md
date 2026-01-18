# CRUD Operations Documentation

This document records Create, Retrieve, Update, and Delete operations performed on the Book model using the Django shell.

## Create
- Created a book titled "1984" by George Orwell (1949):
```python
Book.objects.create(title="1984", author="George Orwell", publication_year=1949)

#Retrieved the book details:
Book.objects.get(title="1984")

#Updated the book title to "Nineteen Eighty-Four"
b = Book.objects.get(title="1984")
b.title = "Nineteen Eighty-Four"
b.save()

#Deleted the book and confirmed deletion:
b.delete()
Book.objects.all()  # Should return an empty queryset
