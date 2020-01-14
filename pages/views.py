from django.shortcuts import render

from .models import Note


def home(request):
    notes = Note.objects.order_by('-last_updated')
    context = {
        'notes': notes,
    }
    return render(request, 'pages/home.html', context)


def note_details(request, note_id):
    note = Note.objects.get(pk=note_id)
    context = {
        'note': note,
    }
    return render(request, 'pages/note_details.html', context)

# def portfolio(request):
#     return render(request, 'pages/portfolio.html')
