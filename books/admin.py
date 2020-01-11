from django.contrib import admin

from .models import Book


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'due_date')
    list_editable = ('status', 'due_date')

admin.site.register(Book, BookAdmin)
