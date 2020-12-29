from django.shortcuts import render
from django.views.generic import ListView,DetailView
from testapp.models import Book
# Create your views here.

class BookListView(ListView):
    model=Book
        # default template name" book_list.html"
        # default context object name "book_list"
        #we can define our own name for template and context
    # template_name='testapp/books.html'
    # context_object_name='books'

class BookDetailView(DetailView):
    model=Book
    # default template name" book_detail.html"
    # default context object name "book or object"
