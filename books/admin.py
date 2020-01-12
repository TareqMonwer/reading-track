from django.contrib import admin

from .models import Book, Blog


class BookAdmin(admin.ModelAdmin):
    list_display = ('name', 'status', 'priority', 'due_date')
    list_editable = ('status', 'due_date')


class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'priority', 'due_date', 'status')
    list_editable = ('due_date', 'status')



admin.site.register(Book, BookAdmin)
admin.site.register(Blog, BlogAdmin)