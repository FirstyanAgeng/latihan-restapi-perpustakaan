from rest_framework import serializers
from .models import User, BookCategory, BookSubCategory, Book

class UserSerializer(serializers.ModelSerializer):
    class Meta: 
        model = User
        fields = '__all__'

class BookCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = BookCategory
        fields = '__all__'

class BookSubCategorySerializer(serializers.ModelSerializer):
    class Meta: 
        model = BookSubCategory
        fields = '__all__'

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate_book_code(self, value):
        # Pastikan bahwa nilai book_code adalah unik dalam tabel Book
        existing_books = Book.objects.exclude(pk=self.instance.pk)  # Exclude current instance
        if existing_books.filter(book_code=value).exists():
            raise serializers.ValidationError("kode buku sudah ada, silahkan masukan kode yang baru")
        return value
