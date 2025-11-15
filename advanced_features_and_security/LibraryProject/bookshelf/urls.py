# bookshelf/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_list, name='book-list'),
    path('add/', views.book_add, name='book-add'),
    path('<int:pk>/edit/', views.book_edit, name='book-edit'),
    path('<int:pk>/delete/', views.book_delete, name='book-delete'),
]