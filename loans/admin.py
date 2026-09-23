from django.contrib import admin
from .models import Loan

class LoanAdmin(admin.ModelAdmin):
    fields = ["user", "book"]
    list_display = ["user", "book", "borrowed_at", "due_date", "returned_at", "created_at"]
    
    
admin.site.register(Loan, LoanAdmin)
