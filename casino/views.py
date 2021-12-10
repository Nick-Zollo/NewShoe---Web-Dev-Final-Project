import datetime

from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm
from .models import Balance, AllWithdraws, AllDeposits


# Create your views here.
def index(request):
    return render(request, 'index.html',)


@login_required()
def indexLogged(request):
    player = Balance.objects.get(user=request.user)
    return render(request, 'index.html', {'player': player})


@login_required()
def fruitSpin(request):
    player = Balance.objects.get(user=request.user)
    return render(request, 'fruitSpin.html', {'player': player})


@login_required()
def updateBalFromSlot(request):
    player = Balance.objects.get(user=request.user)
    if request.method == 'POST':
        slotBalance = request.POST.get('slotBalance')
        newBal = int(slotBalance)
        Balance.objects.update(balance=newBal)
        return redirect('indexLogged')
    return render(request, 'fruitSpin.html', {'player': player})


@login_required()
def hiddenTreasure(request):
    player = Balance.objects.get(user=request.user)
    return render(request, 'hiddenTreasure.html', {'player': player})


@login_required()
def explosiveReels(request):
    player = Balance.objects.get(user=request.user)
    return render(request, 'explosiveReels.html', {'player': player})


# login stuff
def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            Balance.objects.create(user=user)

            return redirect('indexLogged')
    else:
        form = UserCreationForm()

    return render(request, 'accounts/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('indexLogged')
    else:
        form = AuthenticationForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('index')


# Player Balance
@login_required()
def deposit(request):

    player = Balance.objects.get(user=request.user)
    return render(request, 'Balance Management/deposit.html', {'player': player})


@login_required()
def withdraw(request):

    player = Balance.objects.get(user=request.user)
    return render(request, 'Balance Management/withdraw.html', {'player': player})


@login_required()
def depositCustom(request):

    player = Balance.objects.get(user=request.user)
    if request.method == 'POST':
        customAmount = request.POST.get('customAmount')
        newBal = player.balance + int(customAmount)
        Balance.objects.update(balance=newBal)

        # Update Deposits Table
        newDeposit = AllDeposits(depositAmount=customAmount, depositedAt=datetime.date.today(), user=request.user)
        newDeposit.save()
        return redirect('indexLogged')
    return render(request, 'Balance Management/deposit.html', {'player': player})


@login_required()
def withdrawCustom(request):

    player = Balance.objects.get(user=request.user)
    if request.method == 'POST':
        customAmount = request.POST.get('customAmount')
        newBal = player.balance - int(customAmount)
        Balance.objects.update(balance=newBal)

        # Update Withdraws Table
        newWithdraw = AllWithdraws(withdrawAmount=customAmount, withdrewAt=datetime.date.today(), user=request.user)
        newWithdraw.save()
        return redirect('indexLogged')
    return render(request, 'Balance Management/deposit.html', {'player': player})


@login_required()
def allDeposits(request):
    player = Balance.objects.get(user=request.user)
    deposits = AllDeposits.objects.filter(user=request.user)
    context = {'deposits': deposits, 'player': player}
    return render(request, 'Balance Management/allDeposits.html', context)


@login_required()
def allWithdraws(request):
    player = Balance.objects.get(user=request.user)
    withdraws = AllWithdraws.objects.filter(user=request.user)
    context = {'withdraws': withdraws, 'player': player}
    return render(request, 'Balance Management/allWithdraws.html', context)

