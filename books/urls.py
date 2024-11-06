from django.urls import path
from .views import books_list, home_page, book_detail

urlpatterns = [
    path('', home_page, name='home'),
    path('books/', books_list, name='books-list'),
    path('books/<slug:slug>', book_detail, name='book-detail'),
]