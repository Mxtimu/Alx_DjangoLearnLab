**Command:**
```python
from bookshelf.models import Book
# Note: We get the book by its new title
book_to_delete = Book.objects.get(title="Nineteen Eighty-Four")
book_to_delete.delete()

all_books = Book.objects.all()
print(all_books)


# Output: <QuerySet []>
# This confirms the book has been deleted.