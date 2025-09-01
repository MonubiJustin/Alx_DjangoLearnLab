from django.shortcuts import render, get_list_or_404
from django.http import HttpResponse
from django.views.generic import DetailView
from .models import Book, Library

# Create your views here.
# list all books
def book_list(request):
    books = Book.objects.all()
    #Plain text response
    output = "\n".join([f"{book.title} (by {book.author.name})" for book in books])
    return HttpResponse(output, content_type="text/plain")

# show details for a specifuc library
class LibraryDetailView(DetailView):
    model = Library
    template_name = "relationship_app/library_detail.html"
    context_object_name = "library"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Add books of this library to the context
        context["books"] = self.object.books.all() 
        return context
    

