from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_buyers_and_games, name='create_buyers_and_games'),
]