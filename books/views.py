from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Q


def book_list(request):
    search = request.GET.get("s")

    if search:
        books = Book.objects.filter( Q(title__icontains=search) | Q(author__name__icontains=search) )
    else:
        books = Book.objects.all()

    context = {
        "books": books
    }
    
    return render(request, "books/book-list.html", context)


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    is_borrowed = book.loans.filter(user=request.user).exists()
    
    context = {
        "book": book,
        "is_borrowed": is_borrowed
        }
    
    return render(request, "books/book-detail.html", context)



