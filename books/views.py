from django.views.generic import ListView

from .models import Book


class Reading(ListView):
    queryset = Book.objects.filter(status='R')
    context_object_name = 'book_list'
    template_name = 'books/reading.html'


class WishList(ListView):
    queryset = Book.objects.filter(status='W')
    context_object_name = 'book_list'
    template_name = 'books/wishlist.html'


class Completed(ListView):
    queryset = Book.objects.filter(status='C').order_by('-due_date')
    context_object_name = 'book_list'
    template_name = 'books/completed.html'
