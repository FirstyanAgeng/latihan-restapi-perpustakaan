from django.urls import path, include 
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, BookCategoryViewSet, BookSubCategoryViewSet, BookViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'categories', BookCategoryViewSet)
router.register(r'subcategories', BookSubCategoryViewSet)
router.register(r'books', BookViewSet)

urlpatterns = [
    path('', include(router.urls))
]
