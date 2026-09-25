from django.db import models
from django.conf import settings
from books.models import Book
from datetime import timedelta
from django.utils import timezone


def calculate_due_date():
    """
    It calculates the due date and returns the date that is 14 days after the current time.
    """
    
    return timezone.localdate() + timedelta(days=14)


class Loan(models.Model):
    """
    it represend a loan model in datebase
    """
    
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT, related_name="loans")
    book = models.ForeignKey(Book, on_delete=models.PROTECT, related_name="loans")
    
    borrowed_at = models.DateTimeField(auto_now_add=True)
    
    # the due date , it calculate in calculate_due_date function 
    # and is set to 14 days after the current time.
    due_date = models.DateField(default=calculate_due_date)
    
    returned_at = models.DateTimeField(null=True, blank=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.book.title}"
    
