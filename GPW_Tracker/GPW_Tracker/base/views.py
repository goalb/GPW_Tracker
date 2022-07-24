from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect, HttpResponse
from .forms import PortfolioForm, PortfolioFormAdmin
from .models import Portfolio, Company
from django.contrib.auth.models import User
import csv
from django.contrib import messages
from django.core.paginator import Paginator

# from django.contrib.auth import authenticate, login, logout

# Create your views here.


def loginpage(request):
    return render(request, 'login_register.html')


def home(request):
    return render(request, 'home.html')

    # Everything with company --------------------------------------------


def list_company(request):
    list_company = Company.objects.all().order_by('name')
    return render(request, 'base/company.html', {'show_company': list_company})


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

    # Everything with portfolio ----------------------------------------------


def add_portfolio(request):
    submitted = False
    if request.method == "POST":
        if request.user.is_superuser:
            form = PortfolioFormAdmin(request.POST)
            if form.is_valid():
                form.save()
                return HttpResponseRedirect('/add_portfolio?submitted=True')
        else:
            form = PortfolioForm(request.POST)
            if form.is_valid():
                portfolio = form.save(commit=False)
                portfolio.user = request.user.id  # tu coś może być
                portfolio.save()
                # Going back to the page
                return HttpResponseRedirect('/add_portfolio?submitted=True')
    else:
        if request.user.is_superuser:
            form = PortfolioFormAdmin
        else:
            form = PortfolioForm

        if 'submitted' in request.GET:
            submitted = True
        # Success message
    return render(request, 'base/add_portfolio.html', {'form': form, 'submitted': submitted})


def list_portfolio(request):
    list_portfolio = Portfolio.objects.all().order_by('name')

    # Pagination
    p = Paginator(list_portfolio, 3)
    page = request.GET.get('page')
    portfolios = p.get_page(page)

    return render(request, 'base/portfolio.html', {'show_portfolio': list_portfolio, 'portfolios': portfolios})


def show_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    portfolio_owner = User.objects.get(pk=portfolio.user)
    return render(request, 'base/show_portfolio.html', {'portfolio': portfolio, 'portfolio_owner': portfolio_owner})


def search_portfolio(request):
    if request.method == "POST":
        searched = request.POST['searched']
        portfolios = Portfolio.objects.filter(name__contains=searched)
        return render(request, 'base/search_portfolio.html', {'searched': searched, 'portfolios': portfolios})
    else:
        return render(request, 'base/search_portfolio.html', {})


def update_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    form = PortfolioForm(request.POST or None, instance=portfolio)
    if form.is_valid():
        form.save()
        return redirect('list-portfolio')
    return render(request, 'base/update_portfolio.html', {'portfolio': portfolio, 'form': form})


def delete_portfolio(request, portfolio_id):
    portfolio = Portfolio.objects.get(pk=portfolio_id)
    if request.user == portfolio.user:
        portfolio.delete()
        messages.success(request, ("Portfolio deleted"))
        return redirect('list-portfolio')
    else:
        messages.success(request, ("You are not allowed to remoce this portfolio"))
        return redirect('list-portfolio')


def portfolio_text(request):
    response = HttpResponse(content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename=portoflio.txt'

    # Designate model
    portfolios = Portfolio.objects.all()
    lines = []

    # Loop through
    for portfolio in portfolios:
        lines.append(f'{portfolio}\n')

    # Write to textfile
    response.writelines(lines)
    return response


def portfolio_download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename=portoflio.csv'

    # Create a csv writer
    writer = csv.writer(response)

    # Designate model
    portfolios = Portfolio.objects.all()

    # Add column to csv file
    writer.writerow(['Portfolio Name', 'User'])

    # Loop through
    for portfolio in portfolios:
        writer.writerow([portfolio.name, portfolio.user])

    return response

