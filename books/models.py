from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=200)
    
    
    def __str__(self):
        return self.name



class Book(models.Model):
    title = models.CharField(max_length=200)
    
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    category = models.ManyToManyField(Category, blank=True)
    
    total_copies = models.PositiveIntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title
    
    
    def available_copies(self):
        active_loans = self.loans.filter(returned_at__isnull=True).count()
        
        return self.total_copies - active_loans
    
    
    def categorys_for_book(self):
        return ", ".join([cat.name for cat in self.category.all() ])
    categorys_for_book.short_description = "category"
    
    
    class Meta:
        ordering = ["-created_at"]