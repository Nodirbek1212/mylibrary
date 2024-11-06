from django.shortcuts import render
from .models import Book

def home_page(request):
    latest_book = Book.objects.last()
    return render(request, 'books/home.html', {
        'book':latest_book
    })

def books_list(request):
    books = Book.objects.all()
    return render(request, 'books/books_list.html', {
        'books':books
    })

def book_detail(request,slug):
    book = Book.objects.get(slug=slug)
    return render(request, 'books/book_detail.html', {
        'book':book
    })