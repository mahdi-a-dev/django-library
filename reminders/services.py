from django.utils import timezone
from datetime import timedelta
from loans.models import Loan
from .models import Reminder


def create_borrowed_reminders(loan):
    """
    create a reminder when book is borrowed.
    If a borrowed remider already exists for this loan,
    no new reminder will be created.
    """
    reminder_exists = Reminder.objects.filter(
        loan=loan,
        reminder_type="b"
    ).exists()
    
    if not reminder_exists:
        Reminder.objects.create(
            loan=loan,
            reminder_type="b",
            title="Borrowed",
            message=f"The book '{loan.book.title}' was borrowed.",
            )


def create_upcoming_reminders():
    """
    Create reminders for loans whose due date is four days from today.
    Only active loans are considered An existing reminder for the same loan and
    reminder type will not create again.
    """

    today = timezone.localdate()
    target_date = today + timedelta(days=4)
    
    loans = Loan.objects.filter(
        due_date=target_date,
        returned_at__isnull=True
    )
    
    for loan in loans:
        reminder_exists = Reminder.objects.filter(
            loan=loan,
            reminder_type="u"
        ).exists()
        
        if not reminder_exists:
            Reminder.objects.create(
                loan=loan,
                reminder_type="u",
                title="Approaching deadline",
                message=f"Three days remain until the due date for the book '{loan.book.title}'.",
            )


def create_overdue_reminders():
    """
    Create reminders for active loans whose due date pas passed.
    Only loans that hove not been returned are considered.
    """
    
    today = timezone.localdate()
    
    loans = Loan.objects.filter(
        due_date__lt=today,
        returned_at__isnull=True
    )
    
    for loan in loans:
    
        reminder_exists = Reminder.objects.filter(
            loan=loan,
            reminder_type="o"
        ).exists()
        
        if not reminder_exists:
            Reminder.objects.create(
                loan=loan,
                reminder_type="o",
                title="overdue",
                message=f"The due date for the book '{loan.book.title}' has passed.",
                )


def create_returned_reminders(loan):
    """
    Create reminders that borrowed book is returned.
    If a returned reminder already exists for this loan,
    no duplicate reminder will be created.
    """
    
    reminder_exists = Reminder.objects.filter(
        loan=loan,
        reminder_type="r"
    ).exists()
        
    if not reminder_exists:
        Reminder.objects.create(
            loan=loan,
            reminder_type="r",
            title="Returned",
            message=f"The book '{loan.book.title}' was returned..",
            )
