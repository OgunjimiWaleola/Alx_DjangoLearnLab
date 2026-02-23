from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookList, BookViewSet

# Create router and register ViewSet
router = DefaultRouter()
router.register(r'books_all', BookViewSet, basename='book_all')

urlpatterns = [
    # Existing ListAPIView
    path('books/', BookList.as_view(), name='book-list'),

    # Include all CRUD routes from router
    path('', include(router.urls)),
]


from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    # Existing endpoints
    path('books/', BookList.as_view(), name='book-list'),
    path('', include(router.urls)),

    # Token authentication endpoint
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
]