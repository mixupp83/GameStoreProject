from django.shortcuts import render
from .models import Buyer, Game

def create_buyers_and_games(request):
    # Создание покупателей
    buyer1 = Buyer.objects.create(name='Alice', balance=100.00, age=25)
    buyer2 = Buyer.objects.create(name='Bob', balance=50.00, age=30)
    buyer3 = Buyer.objects.create(name='Charlie', balance=200.00, age=17)

    # Создание игр
    game1 = Game.objects.create(title='Game A', cost=50.00, size=5.0, description='Description A', age_limited=True)
    game2 = Game.objects.create(title='Game B', cost=30.00, size=3.0, description='Description B', age_limited=False)
    game3 = Game.objects.create(title='Game C', cost=40.00, size=4.0, description='Description C', age_limited=True)

    # Связывание покупателей с играми
    game1.buyer.set([buyer1, buyer2])
    game2.buyer.set([buyer1, buyer2, buyer3])
    game3.buyer.set([buyer1, buyer2])

    return render(request, 'task1/success.html')