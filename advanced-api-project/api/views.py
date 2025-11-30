from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer
from django_filters import rest_framework
from rest_framework import filters

class BookListView(generics.ListAPIView):
    """
        Retrieves a list of all books.
        - Includes filtering by title, author, and publication year.
        - Includes searching by title and author name.
        - Includes ordering by title and publication year.
        """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    # This Defines the backends to use
    filter_backends = [
        rest_framework.DjangoFilterBackend,  # Enables strict filtering (e.g., ?year=2023)
        filters.SearchFilter,  # Enables search (e.g., ?search=Harry)
        filters.OrderingFilter  # Enables sorting (e.g., ?ordering=title)
    ]

    # Configure Filtering (DjangoFilterBackend)
    # Allows exact matches on these fields
    filterset_fields = ['title', 'author', 'publication_year']

    # Configure Search (SearchFilter)
    # Allows partial searches. 'author__name' lets you search by the related author's name.
    search_fields = ['title', 'author__name']

    # Configure Ordering (OrderingFilter)
    # Allows sorting by these fields
    ordering_fields = ['title', 'publication_year']

class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves a single book by ID.
    Permission: AllowAny (or ReadOnly) access for details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

class BookCreateView(generics.CreateAPIView):
    """
    Creates a new book.
    Permission: Authenticated users only.
    Custom Behavior: Validates data using BookSerializer before saving.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

    # Example of customization: You could hook into perform_create if needed
    # def perform_create(self, serializer):
    #     serializer.save(created_by=self.request.user)

class BookUpdateView(generics.UpdateAPIView):
    """
    Updates an existing book.
    Permission: Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]

class BookDeleteView(generics.DestroyAPIView):
    """
    Deletes a book.
    Permission: Authenticated users only.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]


# Note: We use IsAuthenticatedOrReadOnly for the list/detail views so anyone can read, but only logged-in users can modify.
# We use IsAuthenticated for the write operations.