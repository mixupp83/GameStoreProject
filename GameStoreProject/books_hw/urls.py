from django.urls import path
from . import views

urlpatterns = [
    path('authors/', views.author_list, name='authors'),
    path('books/', views.book_list, name='books'),
    path('add_author/', views.add_author, name='add_author'),
    path('add_book/', views.add_book, name='add_book'),
]