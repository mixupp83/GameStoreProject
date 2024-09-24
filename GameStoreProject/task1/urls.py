from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shop/', views.shop, name='shop'),
    path('cart/', views.cart, name='cart'),
    path('sign_up/', views.sign_up_by_django, name='sign_up_by_django'),
    path('create/', views.create_buyers_and_games, name='create_buyers_and_games'),
]