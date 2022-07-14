from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('', views.home, name="home"),

]