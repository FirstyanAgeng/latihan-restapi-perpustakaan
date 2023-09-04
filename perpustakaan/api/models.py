from django.db import models
from django.core.validators import RegexValidator

class User(models.Model):
    email = models.EmailField(unique=True)
    fullname = models.CharField(max_length=255)
    phone_regex = RegexValidator(
        regex=r'^628[0-9][9,12]',
        message="Nomor telepon harus dimulai dengan '628' dan memiliki panjang 11 hingga 14 digit",
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=14,
        unique=True,
    )
    role = models.CharField(max_length=10, choices=[('ADMIN','Admin'),('STUDENT','Student')])
    password = models.CharField(max_length=255)

class BookCategory(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(blank=False, upload_to='category_icons/')

    def __str__(self):
        return self.name
    
class BookSubCategory(models.Model):
    category = models.ForeignKey(BookCategory, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    icon = models.ImageField(blank=False, upload_to='subcategory_icons/')

    def __str__(self):
        return self.name

class Book(models.Model):
    subcategory = models.ForeignKey(BookSubCategory, on_delete=models.CASCADE)
    book_code = models.CharField(max_length=255, unique=True)
    book_title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.CharField(max_length=255)
    book_publisher = models.CharField(max_length=255)
    stock_available = models.PositiveIntegerField()

    def __str__(self):
        return self.book_title
    
    