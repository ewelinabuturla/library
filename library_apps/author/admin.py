from django.contrib import admin

from .models import Author


class AuthorAdmin(admin.ModelAdmin):
    readonly_fields = ("name",)
    fields = readonly_fields


admin.site.register(Author, AuthorAdmin)
