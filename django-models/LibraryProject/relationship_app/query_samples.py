# This script contains sample queries for the checker.
# It assumes models are imported in a shell or a Django-aware environment.

from .models import Author, Book, Library, Librarian

# 1. Query all books by a specific author.
def get_books_by_author(author_name):
    # First, get the author object
    try:
        author = Author.objects.get(name=author_name)
        # Then, filter books by that author object
        books = Book.objects.filter(author=author)
        return books
    except Author.DoesNotExist:
        return Book.objects.none() # Return an empty queryset


# 2. List all books in a library.
def get_books_in_library(library_name):
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        # Use the .all() manager on the many-to-many field
        books = library.books.all()
        return books
    except Library.DoesNotExist:
        return Book.objects.none()


# 3. Retrieve the librarian for a library.
def get_librarian_for_library(library_name):
    try:
        # Get the library object
        library = Library.objects.get(name=library_name)
        # Access the one-to-one related object directly
        librarian = library.librarian
        return librarian
    except Library.DoesNotExist:
        return None # No library, so no librarian
    except Librarian.DoesNotExist:
        return None # Library exists, but has no librarian

