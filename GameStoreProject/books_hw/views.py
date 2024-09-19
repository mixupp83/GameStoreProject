from django.shortcuts import render, redirect
from .models import Author, Book
from .forms import AuthorForm, BookForm

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'books/authors.html', {'authors': authors})

def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/books.html', {'books': books})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('authors')
    else:
        form = AuthorForm()
    return render(request, 'books/add_author.html', {'form': form})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('books')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})