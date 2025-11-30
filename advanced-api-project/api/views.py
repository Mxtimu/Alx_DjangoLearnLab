from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .models import Book
from .serializers import BookSerializer

class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Permission: AllowAny (or ReadOnly) access for listing.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

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