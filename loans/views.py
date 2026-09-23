from django.shortcuts import render, redirect, get_object_or_404
from .models import Loan
from datetime import timedelta
from django.utils import timezone
from books.models import Book


def my_loans(request):
    loans = Loan.objects.filter(user=request.user, returned_at__isnull=True)
    
    return render(request, "loans/my-loans.html", {"loans": loans})


def loan_detail(request, pk):
    loan = get_object_or_404(Loan, pk=pk, user=request.user)
    
    return render(request, "loans/loan-detail.html", {"loan": loan})


def borrow_book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    due_date = Loan.calculate_due_date()
    
    active_loan = Loan.objects.filter(
        user=request.user,
        book=book,
        returned_at__isnull=True
        ).exists()
    
    if active_loan:
        error = "you borrowed this book already."
        return render(request, "loans/confirm-borrow-book.html", {"book": book, "error": error})

    
    if request.method == "POST":
        Loan.objects.create(
            user=request.user,
            book=book,
            due_date=due_date
        )
        
        return redirect("loans:my-loans")

    return render(request, "loans/confirm-borrow-book.html", {"book": book, "due_date": due_date})



def return_book(request, book_pk):
    book = get_object_or_404(Book, pk=book_pk)
    
    loan = get_object_or_404(Loan, user=request.user, book=book)
    
    remaning_date = timezone.now() - loan.borrowed_at
    if request.method == "POST":
        loan.returned_at = timezone.now()
        loan.save()
        return redirect("accounts:profile")

    return render(
        request,
        "loans/confirm-return-book.html",
        {"book": book, "remaning_date": remaning_date}
    )

