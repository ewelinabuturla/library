from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from .models import Book


def books_list(request):
    books = Book.objects.select_related("author").all()
    data = {
        "count": len(books),
        "results": list(books.values("title", "isbn", "genre", "author__name")),
    }
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})


def book_detail(request, title):
    book = get_object_or_404(Book, title=title)

    data = {
        "title": book.title,
        "isbn": book.isbn,
        "genre": book.genre,
        "author": book.author.name,
        "opinions": [
            {"rating": opinion.rating, "description": opinion.description}
            for opinion in book.opinions.all()
        ],
    }
    return JsonResponse(data, json_dumps_params={"ensure_ascii": False})
