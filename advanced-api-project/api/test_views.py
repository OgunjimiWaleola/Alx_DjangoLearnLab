from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User

from .models import Author, Book


class BookAPITestCase(APITestCase):
    """
    Test suite for Book API endpoints.
    Covers CRUD operations, filtering, searching,
    ordering, and permission enforcement.
    """

    def setUp(self):
        """
        Set up test data and authenticated user.
        This runs before every test.
        """
        self.user = User.objects.create_user(
            username="testuser",
            password="testpassword"
        )

        self.author = Author.objects.create(name="Test Author")

        self.book = Book.objects.create(
            title="Test Book",
            publication_year=2020,
            author=self.author
        )

        self.list_url = "/api/books/"
        self.create_url = "/api/books/create/"
        self.detail_url = f"/api/books/{self.book.id}/"
        self.update_url = f"/api/books/update/{self.book.id}/"
        self.delete_url = f"/api/books/delete/{self.book.id}/"

    
    # READ TESTS (PUBLIC)
    

    def test_get_books_list(self):
        """Test retrieving list of books (unauthenticated)."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_single_book(self):
        """Test retrieving a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["title"], "Test Book")

    
    # CREATE TESTS (AUTH REQUIRED)
    

    def test_create_book_authenticated(self):
        """Test creating a book when authenticated."""
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "New Book",
            "publication_year": 2021,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_book_unauthenticated(self):
        """Test creating a book without authentication."""
        data = {
            "title": "Unauthorized Book",
            "publication_year": 2022,
            "author": self.author.id
        }

        response = self.client.post(self.create_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    
    # UPDATE TESTS
    

    def test_update_book_authenticated(self):
        """Test updating a book when authenticated."""
        self.client.login(username="testuser", password="testpassword")

        data = {
            "title": "Updated Book",
            "publication_year": 2023,
            "author": self.author.id
        }

        response = self.client.put(self.update_url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    
   
   
    
    
     # DELETE TESTS
    
    def test_delete_book_authenticated(self):
        """Test deleting a book when authenticated."""
        self.client.login(username="testuser", password="testpassword")

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    
    # FILTER, SEARCH & ORDER TESTS
    

    def test_filter_books_by_title(self):
        """Test filtering books by title."""
        response = self.client.get(f"{self.list_url}?title=Test Book")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_search_books(self):
        """Test searching books by title."""
        response = self.client.get(f"{self.list_url}?search=Test")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_order_books_by_publication_year(self):
        """Test ordering books by publication year."""
        response = self.client.get(f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)