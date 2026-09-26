from django.urls import path
from . import views

app_name = "loans"

urlpatterns = [
    # ex loans/my_loans
    path("my_loans/", views.my_loans, name="my-loans"),
    # loans/1
    path("<int:pk>/", views.loan_detail, name="loan-detail"),
    # ex: loan/borrow/2
    path("borrow/<int:book_pk>/", views.borrow_book, name="borrow"),
    # ex: loan/2/return
    path("<int:book_pk>/return/", views.return_book, name="return")
]
