from django.db import models
from loans.models import Loan


def get_user_reminders(user):
    """
    its get the user's books reminders
    """
    return Reminder.objects.filter(loan__user=user, is_read=False)


class Reminder(models.Model):
    """
    It represend a reminder model in datebase.
    """
    
    # The reminder types 
    REMINDER_TYPE_CHOICES = (
        ("b", "borrowed"),
        ("u", "upcoming"),
        ("o", "Overdue"),
        ("r", "returned")
    )
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, related_name="reminders")
    
    # title of the reminder massage
    title = models.CharField(max_length=200, default="")
    
    # body of reminder messaege
    message = models.TextField()
    
    # its meaning thad the user has seen this reminder
    is_read = models.BooleanField(default=False)
    
    reminder_type = models.CharField(max_length=1, choices=REMINDER_TYPE_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.get_reminder_type_display()} - {self.loan}"
    
    
    class Meta:
        ordering = ["-created_at"]

