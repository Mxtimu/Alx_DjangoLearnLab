from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.contrib.auth.models import User
from .models import Book, Author


class BookAPITests(APITestCase):

    def setUp(self):
        """
        Set up the test environment.
        This runs before EACH test method.
        """
        # 1. Create a user for authentication tests
        self.user = User.objects.create_user(username='testuser', password='password')

        # 2. Create an author
        self.author = Author.objects.create(name="J.K. Rowling")

        # 3. Create a book to test with
        self.book = Book.objects.create(
            title="Harry Potter",
            publication_year=2001,
            author=self.author
        )

        # 4. Define URLs (using the names we set in urls.py)
        self.list_url = reverse('book-list')
        self.detail_url = reverse('book-detail', kwargs={'pk': self.book.pk})
        self.create_url = reverse('book-create')
        self.update_url = reverse('book-update', kwargs={'pk': self.book.pk})
        self.delete_url = reverse('book-delete', kwargs={'pk': self.book.pk})

    # --- CRUD TESTS ---

    def test_list_books(self):
        """Test retrieving the list of books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # We created 1 book in setUp, so list should have length 1
        self.assertEqual(len(response.data), 1)

    def test_create_book_authenticated(self):
        """Test creating a book while logged in."""
        self.client.force_authenticate(user=self.user)  # Log in the user
        data = {
            "title": "Fantastic Beasts",
            "publication_year": 2016,
            "author": self.author.id
        }
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 2)  # 1 from setUp + 1 new

    def test_update_book(self):
        """Test updating a book."""
        self.client.force_authenticate(user=self.user)
        data = {
            "title": "Harry Potter and the Philosopher's Stone",
            "publication_year": 2001,
            "author": self.author.id
        }
        response = self.client.put(self.update_url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book.refresh_from_db()  # Refresh data from DB
        self.assertEqual(self.book.title, "Harry Potter and the Philosopher's Stone")

    def test_delete_book(self):
        """Test deleting a book."""
        self.client.force_authenticate(user=self.user)
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 0)

    # --- PERMISSION TESTS ---

    def test_create_book_unauthenticated(self):
        """Test that unauthenticated users cannot create books."""
        # We do NOT authenticate here
        data = {"title": "Hacker Book", "publication_year": 2022, "author": self.author.id}
        response = self.client.post(self.create_url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_delete_book_unauthenticated(self):
        """Test that unauthenticated users cannot delete books."""
        response = self.client.delete(self.delete_url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    # --- FILTERING, SEARCH, ORDERING TESTS ---

    def test_filter_books(self):
        """Test filtering books by publication year."""
        # Create a second book with a different year
        Book.objects.create(title="Old Book", publication_year=1950, author=self.author)

        # Filter for the year 2001 (from setUp)
        response = self.client.get(self.list_url, {'publication_year': 2001})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_search_books(self):
        """Test searching books by title."""
        Book.objects.create(title="Lord of the Rings", publication_year=1954, author=self.author)

        # Search for 'Harry'
        response = self.client.get(self.list_url, {'search': 'Harry'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], "Harry Potter")

    def test_ordering_books(self):
        """Test ordering books by publication year."""
        book2 = Book.objects.create(title="Future Book", publication_year=2025, author=self.author)

        # Order by year ascending
        response = self.client.get(self.list_url, {'ordering': 'publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'], "Harry Potter")  # 2001
        self.assertEqual(response.data[1]['title'], "Future Book")  # 2025