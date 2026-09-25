from django.utils import timezone
from datetime import timedelta
from loans.models import Loan
from .models import Reminder


def create_borrowed_reminders(loan):
       
    Reminder.objects.get_or_create(
        loan=loan,
        reminder_type="b",
        title="Borrowed",
        message=f"The book {loan.book.title} was borrowed.",
        )


def create_upcoming_reminders():
    today = timezone.localdate()
    target_date = today + timedelta(days=4)
    
    loans = Loan.objects.filter(
        due_date=target_date,
        returned_at__isnull=True
    )
    
    for loan in loans:
        Reminder.objects.get_or_create(
            loan=loan,
            reminder_type="b",
            title="Approaching deadline",
            message=f"Three days remain until the due date for the book {loan.book.title}.",
        )


def create_overdue_reminders():
    today = timezone.localdate()
    
    loans = Loan.objects.filter(
        due_date__lt=today,
        returned_at__isnull=True
    )
    
    for loan in loans:
        Reminder.objects.get_or_create(
            loan=loan,
            reminder_type="o",
            title="overdue",
            message=f"The due date for the book {loan.book.title} has passed.",
            )


def create_returned_reminders(loan):
  
    Reminder.objects.get_or_create(
        loan=loan,
        reminder_type="r",
        title="Returned",
        message=f"The book {loan.book.title} was returned..",
        )
