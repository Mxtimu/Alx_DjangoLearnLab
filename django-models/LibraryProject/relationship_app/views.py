from django.shortcuts import render
from django.views.generic import DetailView
from .models import Book, Library

# 1. Implement Function-based View (FBV)
def list_books(request):
    """
    Lists all books stored in the database.
    """
    # Get all book objects from the database
    books = Book.objects.all()

    # Create a context dictionary to pass data to the template
    context = {
        'books': books
    }

    # Render the request using our new template
    return render(request, 'relationship_app/list_books.html', context)


# 2. Implement Class-based View (CBV)
class LibraryDetailView(DetailView):
    """
    Displays details for a specific library (by its Primary Key).
    """
    model = Library
    template_name = 'relationship_app/library_detail.html'

    # Django's DetailView automatically finds the library by its <pk>
    # and passes it to the template as 'library' (or 'object')
    context_object_name = 'library'