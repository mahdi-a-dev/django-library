from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Reminder, get_user_reminders


@login_required
def my_reminders(request):
    """
    Display a list of user's reminders.
    User have to be authenticated to see this view.
        
    Args: 
        request: a HttpRequest object.
            
    Returns:
        HttpRespones: The rendered user reminder page.
    """
    reminders = get_user_reminders(request.user)
    
    context = {
        "reminders": reminders
    }
    
    return render(request, "reminders/my-reminders.html", context)



@login_required
def reminder_detail(request, pk):
    """
    Display a reminder of a user.
    User have to be authenticated to see this view.
    
    This method find a user reminder and displayed it in a page,
    And update the reminder field 'is_read' to True,
    so it meaning that the user read reminder and no need to
    see this reminder again.
        
    Args: 
        request: a HttpRequest object.
        pk: reminder primary key
            
    Returns:
        HttpRespones: The rendered user reminder datails page.
    """
    reminder = get_object_or_404(Reminder, pk=pk)
    
    reminder.is_read = True
    reminder.save(update_fields=["is_read"])
    
    context = {
        "reminder": reminder
    }
    return render(request, "reminders/reminder-detail.html", context)