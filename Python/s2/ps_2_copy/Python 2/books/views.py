from django.shortcuts import render
from django.utils import timezone
from books.models import Book, Author, Event
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView
from django.views.generic import TemplateView

# Create your views here.


class BookDetailView(DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookView(ListView):
    model = Book
    template_name = 'books/book_view.html'


class AddBook(CreateView):
    model = Book
    template_name = 'books/add_book.html'
    fields = ["title", 'author','num_pages','published_date','hard_cover']

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['authors'] = Author.objects.all()
        return data


class EventShow(TemplateView):
    model = Book
    template_name = 'books/event_view.html'

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['events'] = Event.objects.filter(start_date__lte=timezone.now(), end_date__gte=timezone.now())
        return data

