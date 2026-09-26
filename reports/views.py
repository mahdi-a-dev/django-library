from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from books.models import Book
from django.contrib.auth.models import User
from loans.models import Loan
from reminders.models import Reminder


@login_required
def reports(request):
    """
    Display a report page for admins.
    Regular users do not have access to this page, even if they are authenticated.
    
    This method provides a summary report on the number of books, loans, 
    active loans, reminders, and unread reminders, 
    and displays all reminders in detail.
        
    Args: 
        request: a HttpRequest object.
            
    Returns:
        HttpRespones: The rendered report page.
    """
    
    if not request.user.is_staff:
        return redirect("books:book-list")
    
    book_count = Book.objects.count()
    user_count = User.objects.filter(is_staff=False).count()
    loan_count = Loan.objects.count()
    loan_active_count = Loan.objects.filter(returned_at__isnull=True).count()
    reminder_count = Reminder.objects.count()
    
    read_reminder_count = Reminder.objects.filter(is_read=True).count()
    unread_reminder_count = Reminder.objects.filter(is_read=False).count()
    
    reminders = Reminder.objects.select_related(
        "loan",
        "loan__user",
        "loan__book",
    ).order_by("-created_at")
    
    
    context = {
        "book_count" : book_count,
        "user_count" : user_count,
        "loan_count": loan_count,
        "loan_active_count" : loan_active_count,
        "reminder_count" : reminder_count,
        "read_reminder_count" : read_reminder_count,
        "unread_reminder_count": unread_reminder_count,
        
        "reminders": reminders
    }
    
    return render(request, "reports/reports.html", context)
