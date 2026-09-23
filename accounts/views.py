from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import LoginForm, CreateForm


def register(request):
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


def profile(request):
    if request.user.is_authenticated:
        return render(request, "registration/profile.html")
    return redirect("accounts:login")



def login_view(request):
    if request.method == "POST":
        form = LoginForm(
            request,
            data=request.POST
        )
        
        if form.is_valid():
            login(request, form.get_user())
            
            return redirect("books:book-list")
        
    else:
        form = LoginForm(request)
    
    context = {
        "form": form
    }
        
    return render(request, "registration/login.html", context)


def logout_view(request):
    logout(request)
    return redirect("books:book-list")


