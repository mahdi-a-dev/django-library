from django.shortcuts import render, get_object_or_404
from .models import Book
from django.core.paginator import Paginator



def book_list(request, page=1):
    """
    Display a pagianted list of book.
    
    Args: 
        request: a HttpRequest object.
        page: The page number to dispaly. default to 1.
        
    Returns:
        HttpRespones: The rendered book list page.
    """
    
    books_list = Book.objects.all()
    paginator = Paginator(books_list, 4)
    books = paginator.get_page(page)

    context = {
        "books": books
    }
    
    return render(request, "books/book-list.html", context)


def book_detail(request, pk):
    """
    Display a details of a specific book.
    
    Args: 
        request: a HttpRequest object.
        pk: The primary key of the  requested book.
        
    Returns:
        HttpRespones: The rendered book detail page.
        Http404: If the requested book does not exist.
    """
    book = get_object_or_404(Book, pk=pk)
    
    if request.user.is_authenticated:
        # Check whether the user currently has an active loan
        is_borrowed = book.loans.filter(user=request.user, returned_at__isnull=True).exists()
    else:
        is_borrowed = False
    
    context = {
        "book": book,
        "is_borrowed": is_borrowed
        }
    
    return render(request, "books/book-detail.html", context)



