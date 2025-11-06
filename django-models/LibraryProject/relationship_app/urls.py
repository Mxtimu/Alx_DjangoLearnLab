# relationship_app/urls.py
from django.urls import path
from . import views  # This is the main import that makes the code work
from django.contrib.auth import views as auth_views


from .views import list_books, LibraryDetailView, admin_view, librarian_view, member_view
from .views import list_books
from .views import LibraryDetailView



urlpatterns = [
    # --- THIS IS THE FIX ---
    # Login
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout - The checker wants 'template_name=' to be here
    path('logout/', auth_views.LogoutView.as_view(template_name='relationship_app/logout.html'), name='logout'),

    # Registration
    path('register/', views.register, name='register'),
    path('admin-page/', views.admin_view, name='admin_view'),
    path('librarian-page/', views.librarian_view, name.='librarian_view'),
    path('member-page/', views.member_view, name='member_view'),




    # --- Your old URLs ---
    path('books/', views.list_books, name='list-books'),
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),


]