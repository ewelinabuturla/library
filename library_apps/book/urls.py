from django.urls import path

from .views import book_detail, books_list

app_name = "book"

urlpatterns = [
    path("books/", books_list, name="list"),
    path("books/<str:title>/", book_detail, name="detail"),
]
