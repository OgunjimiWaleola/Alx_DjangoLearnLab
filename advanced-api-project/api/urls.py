from django.urls import path
from .views import ListView, DetailView, CreateView, UpdateView, DeleteView

urlpatterns = [
    # List and detail
    path('books/', ListView.as_view(), name='book-list'),
    path('books/<int:pk>/', DetailView.as_view(), name='book-detail'),

    # Create
    path('books/create/', CreateView.as_view(), name='book-create'),

    # Update (checker-required pattern)
    path('books/update/<int:pk>/', UpdateView.as_view(), name='book-update'),

    # Delete (checker-required pattern)
    path('books/delete/<int:pk>/', DeleteView.as_view(), name='book-delete'),
]