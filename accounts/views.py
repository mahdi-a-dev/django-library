from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from .forms import LoginForm, CreateForm
from django.contrib.auth.decorators import login_required
from reminders.models import get_user_reminders


def register(request):
    """
    Register a new user account.
    
    On successful registration , the new user
    is automatically logged in and redirected to the profile page.
    
    Args:
        request: The HTTP request object.
    
    Returns:
        HttpRespones: The rendered registration page.
        HttpResponesRedirect: Redirect to the profie page after successful registration.
    """
    
    if request.method == "POST":
        form = CreateForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            login(request, user)
            
            return redirect("accounts:profile")
        
    else:
        form = CreateForm()
    
    context = {
        "form": form
    }
        
    return render(request, "registration/register.html", context)


@login_required
def profile(request):
    """
    Display the profile page for the authenticated user.
    
    Args:
        request: The HTTP request object.
            
    Returns:
        HttpRespones: The rendered profile page.
    """
    
    reminders = get_user_reminders(request.user)[:3]
    
    context = {
        "reminders": reminders
    }
    
    return render(request, "registration/profile.html", context)



def login_view(request):
    """
    Authenticate a user and log them into the application.
    
    Args:
        request: The HTTP request object.
            
    Returns:
        HttpRespones: The rendered login page.
        HttpResponesRedirect: Redirect to th book list after successful authentication.
    """
    
    if request.method == "POST":
        form = LoginForm(
            request,
            data=request.POST
        )
        
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            
            # redirect admin user to admin panel
            if user.is_staff:
                return redirect("/admin/")
            
            return redirect("books:book-list")
  
    else:
        form = LoginForm(request)
    
    context = {
        "form": form
    }
        
    return render(request, "registration/login.html", context)


def logout_view(request):
    """
    Logout the current user and redirect to the book list.
    
    Args:
        request: The HTTP request object.
            
    Returns:
        HttpResponesRedirect: Redirect to th book list
    """
    logout(request)
    return redirect("books:book-list")


