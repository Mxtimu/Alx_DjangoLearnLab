from django.urls import path, include # <--- Import include
from rest_framework.routers import DefaultRouter # <--- Import DefaultRouter
from .views import BookList, BookViewSet

# this is done to Create a router instance
router = DefaultRouter()



router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [

    path('books/', BookList.as_view(), name='book-list'),

    # Include the router URLs for BookViewSet
    path('', include(router.urls)),
]