from django.urls import path
from django.conf.urls.static import static
from django.urls import path
from . import views
from .views import home

urlpatterns = [
    path('', home),
    path('authors/', views.author_list, name='author_list'),
    path('books/', views.book_list, name='book_list'),
    path('reviews/', views.review_list, name='review_list'),
]