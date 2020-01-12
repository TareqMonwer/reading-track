from django.views.generic import ListView

from .models import Book, Blog


class Reading(ListView):
    queryset = Book.objects.filter(status='R')
    context_object_name = 'book_list'
    template_name = 'books/reading.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(status='R')
        context['blogs'] = blogs
        return context


class WishList(ListView):
    queryset = Book.objects.filter(status='W')
    context_object_name = 'book_list'
    template_name = 'books/wishlist.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blogs = Blog.objects.filter(status='W')
        context['blogs'] = blogs
        return context


class Completed(ListView):
    queryset = Book.objects.filter(status='C').order_by('-due_date')
    context_object_name = 'book_list'
    template_name = 'books/completed.html'
