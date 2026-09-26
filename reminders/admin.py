from django.contrib import admin
from .models import Reminder

class ReminderAdmin(admin.ModelAdmin):
    list_display = ["loan", "title", "message", "is_read", "reminder_type", "created_at"]
    list_filter = ["is_read", "reminder_type"]
    search_fields = ["title", "message"]
    date_hierarchy = "created_at"
    
    
admin.site.register(Reminder, ReminderAdmin)
