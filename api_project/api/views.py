from rest_framework import generics, viewsets
from .models import Book
from .serializers import BookSerializer

class BookList(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    """
    This ViewSet provides the standard actions:
    list, create, retrieve, update, and destroy.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
