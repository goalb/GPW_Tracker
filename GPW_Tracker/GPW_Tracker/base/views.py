from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from .forms import PortfolioForm
from .models import Portfolio, Company


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


def list_company(request):
    list_company = Company.objects.all()
    return render(request, 'base/company.html', {'show_company': list_company})


def show_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    return render(request, 'base/show_portfolio.html', {'portfolio': portfolio})


def show_company(request, company_id):
    company = Company.objects.get(pk=company_id)
    return render(request, 'base/show_company.html', {'company': company})


def search_company(request):
    if request.method == "POST":
        searched = request.POST['searched']
        companies = Company.objects.filter(name__contains=searched)
        return render(request, 'base/search_company.html', {'searched': searched, 'companies': companies})
    else:
        return render(request, 'base/search_company.html', {})


def update_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    form = PortfolioForm(request.POST or None, instance=portfolio)
    if form.is_valid():
        form.save()
        return redirect('list-portfolio')
    return render(request, 'base/update_portfolio.html', {'portfolio': portfolio, 'form': form})

