from django.contrib import admin
from .models import Loan

class LoanAdmin(admin.ModelAdmin):
    fields = ["user", "book"]
    list_display = ["user", "book", "borrowed_at", "due_date", "returned_at"]
    list_filter = ["returned_at", "due_date"]
    search_fields = ["user__username", "book__title"]
    date_hierarchy = "borrowed_at"
    
    
admin.site.register(Loan, LoanAdmin)
