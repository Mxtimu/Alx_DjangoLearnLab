**Command:**
```python
from bookshelf.models import Book
# Get the book by its new title, using the 'book' variable
book = Book.objects.get(title="Nineteen Eighty-Four")
book.delete()

# Confirm by trying to retrieve all books
all_books = Book.objects.all()
print(all_books)

# Output: <QuerySet []>
# This confirms the book has been deleted.