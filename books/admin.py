from django.contrib import admin
from .models import Book, Author, Category


class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "author", "categorys_for_book", "total_copies", "created_at", "updated_at"]


class AuthorAdmin(admin.ModelAdmin):
    list_display = ["name"]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ["name"]
    
    
admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
