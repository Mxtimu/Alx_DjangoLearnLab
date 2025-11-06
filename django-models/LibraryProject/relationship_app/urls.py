# relationship_app/urls.py
from django.urls import path
from . import views  # This is the main import that makes the code work
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView



from .views import list_books
from .views import LibraryDetailView



urlpatterns = [

    # Login
    path('login/', auth_views.LoginView.as_view(template_name='relationship_app/login.html'), name='login'),

    # Logout
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Registration
    path('register/', views.register, name='register'),

    # Page to show after logout
    path('logged_out/', TemplateView.as_view(template_name='relationship_app/logout.html'), name='logged_out'),
    # Route for the function-based view (list all books)
    path('books/', views.list_books, name='list-books'),

    # Route for the class-based view (show one library)
    # <int:pk> is a variable that Django uses to find the library by its ID
    path('library/<int:pk>/', views.LibraryDetailView.as_view(), name='library-detail'),
]