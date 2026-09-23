from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.book_list, name="book-list"),
    path("<str:search>", views.book_list, name="book-search"),
    path("detail/<int:pk>", views.book_detail, name="book-detail")
]
