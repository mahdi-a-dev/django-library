from django.urls import path
from . import views

app_name = "loans"

urlpatterns = [
    path("my_loans/", views.my_loans, name="my-loans"),
    path("<int:pk>/", views.loan_detail, name="loan-detail"),
    path("borrow/<int:book_pk>/", views.borrow_book, name="borrow"),
    path("<int:book_pk>/return/", views.return_book, name="return")
]
