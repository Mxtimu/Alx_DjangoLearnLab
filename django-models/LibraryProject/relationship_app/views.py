from django.shortcuts import render

from django.views.generic.detail import DetailView

from .models import Book
from .models import Library

# 1. Implement Function-based View (FBV)
def list_books(request):
    """
    Lists all books stored in the database.
    """
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'relationship_app/list_books.html', context)


# 2. Implement Class-based View (CBV)
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library (by its Primary Key).
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'