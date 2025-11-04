# Django CRUD Operations for Book Model

This file documents the CRUD operations performed via the Django shell.

## 1. Create

**Command:**
```python
from bookshelf.models import Book
book = Book.objects.create(title="1984", author="George Orwell", publication_year=1949)
print(book)
# Output: 1984
# This confirms the book object was created.

b = Book.objects.get(title="1984")
print(f"Title: {b.title}, Author: {b.author}, Year: {b.publication_year}")

# Output: Title: 1984, Author: George Orwell, Year: 1949
# This shows the book was successfully retrieved.

book_to_update = Book.objects.get(title="1984")
book_to_update.title = "Nineteen Eighty-Four"
book_to_update.save()

updated_book = Book.objects.get(id=book_to_update.id)
print(updated_book.title)

# Output: Nineteen Eighty-Four
# This confirms the book's title has been updated.

book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

all_books = Book.objects.all()
print(all_books)

# Output: <QuerySet []>
# This confirms the book has been deleted.