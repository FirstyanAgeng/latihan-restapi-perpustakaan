from django.contrib import admin
from .models import User, BookCategory, BookSubCategory, Book
# Register your models here.

admin.site.register(User)
admin.site.register(BookCategory)
admin.site.register(BookSubCategory)
admin.site.register(Book)
