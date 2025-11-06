**Command:**
```python
from bookshelf.models import Book
b = Book.objects.get(title="1984")
print(f"Title: {b.title}, Author: {b.author}, Year: {b.publication_year}")

# Output: Title: 1984, Author: George Orwell, Year: 1949
# This shows the book was successfully retrieved.