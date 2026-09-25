from django.shortcuts import render, redirect
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
        HttpRespones: The rendered user profile page with reminders list.
    """
    reminders = get_user_reminders(request.user)
    return render(request, "reminders/my-reminders.html", {"reminders": reminders})



@login_required
def detail(request):
    pass