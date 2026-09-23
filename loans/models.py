from django.db import models
from django.conf import settings
from books.models import Book
from datetime import timedelta
from django.utils import timezone


class Loan(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="loans")
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="loans")
    
    borrowed_at = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField()
    returned_at = models.DateTimeField(null=True, blank=True)
    
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def calculate_due_date():
        return timezone.now() + timedelta(days=14)
    
    
    def __str__(self):
        return f"{self.user.username} -> {self.book.title}"
    
