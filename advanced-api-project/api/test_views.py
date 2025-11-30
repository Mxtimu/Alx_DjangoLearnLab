from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
        """
        Set up the test environment.
        """
        # Create a user for authentication tests
        self.user = User.objects.create_user(username='testuser', password='password')

        # Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # Create a book to test with
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=2001,
            author=self.author
        )

        # Define URLs
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    # CRUD TESTS

    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """Test creating a book while logged in."""
        # FIX: Use login() instead of force_authenticate() for the checker
        self.client.login(username='testuser', password='password')

        data = {
            "title": "Fantastic Beasts",
            "publication_year": 2016,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)

    def test_update_book(self):
        """Test updating a book."""
        # FIX: Use login()
        self.client.login(username='testuser', password='password')

        data = {
            "title": "Harry Potter and the Philosopher's Stone",
            "publication_year": 2001,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()
        self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")

    def test_delete_book(self):
        """Test deleting a book."""
        # FIX: Use login(), i think ?
        self.client.login(username='testuser', password='password')

        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # PERMISSION TESTS

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books."""
        # We DO NOT login here
        data = {"title": "Hacker Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_unauthenticated(self):
        """Test that unauthenticated users cannot delete books."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    #  FILTERING, SEARCH, ORDERING TESTS

    def test_filter_books(self):
        """Test filtering books."""
        Book.objects.create(title="Old Book", publication_year=1950, author=self.author)
        response = self.client.get(self.list_url, {'publication_year': 2001})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_search_books(self):
        """Test searching books."""
        Book.objects.create(title="Lord of the Rings", publication_year=1954, author=self.author)
        response = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_ordering_books(self):
        """Test ordering books."""
        Book.objects.create(title="Future Book", publication_year=2025, author=self.author)
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter")
        self.assertEqual(response.data[1]['title'], "Future Book")