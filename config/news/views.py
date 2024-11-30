from django.shortcuts import render

from django.core.handlers.wsgi import WSGIRequest
from django.http import HttpResponse
from .models import Author, Book, Review

def home(request: WSGIRequest):
    return render(request, 'index.html')

def author_list(request):
    authors = Author.objects.all()
    return render(request, 'author_list.html', {'authors': authors})


def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def review_list(request):
    reviews = Review.objects.all()
    return render(request, 'review_list.html', {'reviews': reviews})
