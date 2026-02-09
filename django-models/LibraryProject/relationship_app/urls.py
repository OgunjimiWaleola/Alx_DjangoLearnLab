from django.urls import path
from .views import (
    list_books,
    LibraryDetailView,
    register,
    CustomLoginView,
    CustomLogoutView,
)

urlpatterns = [
    # Books and Library
    path('books/', list_books, name='list_books'),
    path('library/<int:pk>/', LibraryDetailView.as_view(), name='library_detail'),

    # Authentication URLs
    path('register/', register, name='register'),            # function-based
    path('login/', CustomLoginView.as_view(), name='login'), # class-based
    path('logout/', CustomLogoutView.as_view(), name='logout'), # class-based
]
