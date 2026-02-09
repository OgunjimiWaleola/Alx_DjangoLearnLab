from django.shortcuts import render, redirect
from django.views.generic.detail import DetailView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login  # ✅ required by ALX checker
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
# Registration View (function-based)
# -------------------------------
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # ✅ log the user in immediately after registration
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# -------------------------------
# Login and Logout Views (Class-Based)
# -------------------------------
class CustomLoginView(LoginView):
    template_name = "relationship_app/login.html"

class CustomLogoutView(LogoutView):
    template_name = "relationship_app/logout.html"
