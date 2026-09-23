from django.shortcuts import render, get_object_or_404
from .models import Book


def book_list(request):
    search = request.GET.get("search")

    if search:
        books = Book.objects.filter(
            title__icontains=search
        )
    else:
        books = Book.objects.all()

    return render(
        request,
        "books/book-list.html",
        {"books": books},
    )


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    
    return render(request, "books/book-detail.html", {"book": book})



