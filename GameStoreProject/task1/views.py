from django.shortcuts import render
from .models import Buyer, Game
from .forms import UserRegisterForm
from .models import Buyer

def index(request):
    return render(request, 'task1/index.html')

def shop(request):
    games = Game.objects.all()
    return render(request, 'task1/shop.html', {'games': games})

def cart(request):
    return render(request, 'task1/cart.html')

def create_buyers_and_games(request):
    buyer1 = Buyer.objects.create(name='Alice', balance=100.00, age=25)
    buyer2 = Buyer.objects.create(name='Bob', balance=50.00, age=30)
    buyer3 = Buyer.objects.create(name='Charlie', balance=200.00, age=17)

    game1 = Game.objects.create(title='Game A', cost=50.00, size=5.0, description='Description A', age_limited=True)
    game2 = Game.objects.create(title='Game B', cost=30.00, size=3.0, description='Description B', age_limited=False)
    game3 = Game.objects.create(title='Game C', cost=40.00, size=4.0, description='Description C', age_limited=True)

    game1.buyer.set([buyer1, buyer2])
    game2.buyer.set([buyer1, buyer2, buyer3])
    game3.buyer.set([buyer1, buyer2])

    return render(request, 'task1/success.html')

def sign_up_by_django(request):
    info = {}
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']

            if password != repeat_password:
                info['error'] = 'Пароли не совпадают'
            elif age < 18:
                info['error'] = 'Вы должны быть старше 18'
            elif Buyer.objects.filter(name=username).exists():
                info['error'] = 'Пользователь уже существует'
            else:
                Buyer.objects.create(name=username, balance=0.00, age=age)
                return render(request, 'task1/registration_success.html', {'username': username})
    else:
        form = UserRegisterForm()

    info['form'] = form
    return render(request, 'task1/registration_page.html', info)