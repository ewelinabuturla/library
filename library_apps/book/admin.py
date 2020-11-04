from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    readonly_fields = ("title", "isbn", "genre", "author")
    fields = readonly_fields


admin.site.register(Book, BookAdmin)
