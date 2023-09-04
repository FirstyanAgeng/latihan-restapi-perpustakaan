from rest_framework import viewsets
from .models import User, BookCategory, BookSubCategory, Book
from .serializers import UserSerializer, BookCategorySerializer, BookSubCategorySerializer, BookSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class BookCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookCategory.objects.all()
    serializer_class = BookCategorySerializer

class BookSubCategoryViewSet(viewsets.ModelViewSet):
    queryset = BookSubCategory.objects.all()
    serializer_class = BookSubCategorySerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # Validasi kustom untuk memeriksa keunikan book_code
        book_code = serializer.validated_data.get('book_code')
        if Book.objects.filter(book_code=book_code).exists():
            return Response({"book_code": ["book_code sudah ada, silahkan masukan kode baru."]}, status=status.HTTP_400_BAD_REQUEST)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
