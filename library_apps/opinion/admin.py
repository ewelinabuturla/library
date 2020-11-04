from django.contrib import admin

from .models import Opinion


class OpinionAdmin(admin.ModelAdmin):
    readonly_fields = ("rating", "description", "book")
    fields = readonly_fields


admin.site.register(Opinion, OpinionAdmin)
