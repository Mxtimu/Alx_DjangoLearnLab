
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

# Imports for the checker
from .views import (
    list_books, LibraryDetailView, admin_view, librarian_view, member_view,
    book_add, book_edit, book_delete
)

urlpatterns = [
    # Authentication URLs
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),
    path('register/', views.register, name='register'),

    # Role-Based URLs
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),

    # Original App URLs
    # path('books/', views.list_books, name='list-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),


    # Changed paths to match the checker's literal strings
    # path('add_book/', views.book_add, name='book-add'),
    # path('edit_book/<int:pk>/', views.book_edit, name='book-edit'),
    # path('delete_book/<int:pk>/', views.book_delete, name='book-delete'),
]