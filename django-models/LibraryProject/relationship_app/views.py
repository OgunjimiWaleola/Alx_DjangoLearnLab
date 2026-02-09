from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login  
from .models import Book, Library

# -------------------------------
# Function-Based View: List all books
# -------------------------------
def list_books(request):
    books = Book.objects.all()  
    return render(request, "relationship_app/list_books.html", {"books": books})

# -------------------------------
# Class-Based View: Library Detail
# -------------------------------
class LibraryDetailView(DetailView):
    model = Library  
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"

# -------------------------------
# Registration View
# -------------------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ log in immediately
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})
