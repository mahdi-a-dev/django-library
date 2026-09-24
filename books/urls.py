from django.urls import path
from . import views

app_name = "books"

urlpatterns = [
    path("", views.book_list, name="book-list"),
    # ex: /page/1
    path("page/<int:page>/", views.book_list, name="book-list"),
    # ex: /book/1
    path("book/<int:pk>/", views.book_detail, name="book-detail")
]
