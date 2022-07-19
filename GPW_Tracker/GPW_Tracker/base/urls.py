from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('', views.home, name="home"),
    path('add_portfolio', views.add_portfolio, name='add-portfolio'),
    path('list_portfolio', views.list_portfolio, name='list-portfolio'),
    path('show_portfolio/<portfolio_id>', views.show_portfolio, name='show-portfolio'),
]