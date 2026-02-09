from django.shortcuts import render
from .models import Book, Library
from django.views.generic.detail import DetailView   


# Function-Based View
def list_books(request):
    books = Book.objects.all()  
    return render(request, "relationship_app/list_books.html", {"books": books})



# Class-Based View
from django.views.generic import DetailView
from .models import Library

class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"


# Authentication views
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages

# -------------------------------
# Register View
# -------------------------------
def register_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # log the user in immediately after registration
            messages.success(request, "Registration successful.")
            return redirect('list_books')  # redirect to books page
        else:
            messages.error(request, "Registration failed. Please fix the errors.")
    else:
        form = UserCreationForm()
    return render(request, "relationship_app/register.html", {"form": form})

# -------------------------------
# Login View
# -------------------------------
def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            messages.success(request, "Login successful.")
            return redirect('list_books')
        else:
            messages.error(request, "Login failed. Please check your username and password.")
    else:
        form = AuthenticationForm()
    return render(request, "relationship_app/login.html", {"form": form})

# -------------------------------
# Logout View
# -------------------------------
from django.contrib.auth.decorators import login_required

@login_required
def logout_view(request):
    logout(request)
    return render(request, "relationship_app/logout.html")
