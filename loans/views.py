from django.shortcuts import render, redirect, get_object_or_404
from .models import Loan
from django.utils import timezone
from books.models import Book
from reminders.services import create_returned_reminders, create_borrowed_reminders
from django.contrib.auth.decorators import login_required


@login_required
def my_loans(request):
    """
    Display a list of user's loan.
    User have to be authenticated to see this view.
    
    Args: 
        request: a HttpRequest object.

        
    Returns:
        HttpRespones: The rendered loan list page.
    """
    loans = Loan.objects.filter(user=request.user, returned_at__isnull=True)
    
    context = {
        "loans": loans
        }
        
    return render(request, "loans/my-loans.html", context)
    

@login_required
def loan_detail(request, pk):
    """
    Display a details of a user loan.
    User have to be authenticated to see this view.
       
    Args: 
        request: a HttpRequest object.
        pk: The primary key of the requested loan.
           
    Returns:
        HttpRespones: The rendered loan detail page.
        Http404: If the requested loan does not exist.
        
    """
    loan = get_object_or_404(Loan, pk=pk, user=request.user)
    return render(request, "loans/loan-detail.html", {"loan": loan})


@login_required
def borrow_book(request, book_pk):
    """
    Display a confirm form for borrow user's book.
    User have to be authenticated to see this view.
    
    If book is not available of user already borrowed it, will return error to remplate.
       
    Args: 
        request: a HttpRequest object.
        book_pk: The primary key of the requested book.
           
    Returns:
        HttpRespones: The rendered confirm borrow page.
        Http404: If the requested loan does not exist.
        
    """
    book = get_object_or_404(Book, pk=book_pk)

    if book.available() <= 0:
        error = "This book is not available."
        return render(request, "loans/confirm-borrow-book.html", {"book": book, "error": error})
        
    active_loan = Loan.objects.filter(
        user=request.user,
        book=book,
        returned_at__isnull=True
        ).exists()
    
    if active_loan:
        error = "You borrowed this book already."
        return render(request, "loans/confirm-borrow-book.html", {"book": book, "error": error})
    
    if request.method == "POST":
        loan = Loan.objects.create(
            user=request.user,
            book=book,
        )
        
        create_borrowed_reminders(loan)
        
        return redirect("loans:my-loans")

    return render(request, "loans/confirm-borrow-book.html", {"book": book})
    

@login_required
def return_book(request, book_pk):
    """
    Display a confirm form for return user's book.
    User have to be authenticated to see this view.
       
    Args: 
        request: a HttpRequest object.
        book_pk: The primary key of the requested book.
           
    Returns:
        HttpRespones: The rendered confirm loan return page.
        Http404: If the requested loan does not exist.
        
    """
    book = get_object_or_404(Book, pk=book_pk)
    loan = get_object_or_404(Loan, user=request.user, book=book, returned_at__isnull=True)
    

    if request.method == "POST":
        loan.returned_at = timezone.now()
        loan.save(update_fields=["returned_at"])
        
        # this create a reminder for returend loan
        # Its comes from Reminder.services
        create_returned_reminders(loan)
        
        return redirect("accounts:profile")
   
    return render(
                request,
                "loans/confirm-return-book.html",
                {"book": book}
            )

