from django.urls import path, include # <--- Import include
from rest_framework.routers import DefaultRouter # <--- Import DefaultRouter
from .views import BookList, BookViewSet
from rest_framework.authtoken.views import obtain_auth_token

# this is done to Create a router instance
router = DefaultRouter()



router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [

    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]