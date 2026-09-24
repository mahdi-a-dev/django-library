from django.db import models


class Author(models.Model):
    """
    it represend a author model in database.
    """
    
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name


class Category(models.Model):
    """
        it represend a category model in database.
    """
    
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name



class Book(models.Model):
    """
    it represend a book model in database
    """
    
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, blank=True)
    
    # the total number of the book in the library
    # this value does not change when a book is borrowed or returned.
    total_copies = models.PositiveIntegerField(default=1)
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    
    def available(self):
        """
            Calculate the number of copies currently available for borrowing.
        """
        
        # count all active loans associated with this book
        # a loan is considered active if the book has not been returned yet.
        active_loans = self.loans.filter(returned_at__isnull=True).count()
        
        return self.total_copies - active_loans
    
    
    
    # this method returns all categorys of a book.
    def categorys_for_book(self):
        return [cat.name for cat in self.category.all() ]
    categorys_for_book.short_description = "category"
    
    
    class Meta:
        ordering = ["-created_at"]