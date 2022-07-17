from django.shortcuts import render


# from django.contrib.auth import authenticate, login, logout

# Create your views here.

def loginpage(request):
    return render(request, 'login_register.html')


def home(request):
    return render(request, 'home.html')
