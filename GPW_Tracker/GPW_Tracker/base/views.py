from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import PortfolioForm
from .models import Portfolio


# from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginpage(request):
    return render(request, 'login_register.html')


def home(request):
    return render(request, 'home.html')


def add_portfolio(request):
    submitted = False
    if request.method == "POST":
        form = PortfolioForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/add_portfolio?submitted=True')
    else:
        form = PortfolioForm
        if 'submitted' in request.GET:
            submitted = True

    return render(request, 'base/add_portfolio.html', {'form': form, 'submitted': submitted})


def list_portfolio(request):
    list_portfolio = Portfolio.objects.all()
    return render(request, 'base/portfolio.html', {'show_portfolio': list_portfolio})


def show_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    return render(request, 'base/show_portfolio.html', {'portfolio': portfolio})
