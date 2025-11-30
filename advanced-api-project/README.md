# Advanced API Project Documentation

## Views Configuration

This project uses Django REST Framework Generic API Views to handle CRUD operations for the Book model.

### 1. BookListView (`/books/`)
- **Method:** GET
- **Description:** Returns a list of all books.
- **Permissions:** Read-only access for everyone (IsAuthenticatedOrReadOnly).

### 2. BookDetailView (`/books/<id>/`)
- **Method:** GET
- **Description:** Returns details of a single book.
- **Permissions:** Read-only access for everyone.

### 3. BookCreateView (`/books/create/`)
- **Method:** POST
- **Description:** Adds a new book to the database.
- **Permissions:** Authenticated users only (IsAuthenticated).
- **Customization:** Uses standard serializer validation to ensure publication year is not in the future.

### 4. BookUpdateView (`/books/update/<id>/`)
- **Method:** PUT/PATCH
- **Description:** Modifies an existing book.
- **Permissions:** Authenticated users only.

### 5. BookDeleteView (`/books/delete/<id>/`)
- **Method:** DELETE
- **Description:** Removes a book from the database.
- **Permissions:** Authenticated users only.