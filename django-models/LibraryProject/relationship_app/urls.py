# relationship_app/urls.py
from django.urls import path
from . import views

urlpatterns = [
    # Route for the function-based view (list all books)
    path('books/', views.list_books, name='list-books'),

    # Route for the class-based view (show one library)
    # <int:pk> is a variable that Django uses to find the library by its ID
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]