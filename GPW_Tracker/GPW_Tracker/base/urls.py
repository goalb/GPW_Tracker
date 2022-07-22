from django.urls import path, include
from . import views

urlpatterns = [
    path('login/', views.loginpage, name="login"),
    path('', views.home, name="home"),

    # URLs for app users
    path('users/', include('django.contrib.auth.urls')),
    path('users/', include('users.urls')),

    # Everything with company
    path('show_company/<company_id>', views.show_company, name='show-company'),
    path('search_company', views.search_company, name='search-company'),

    # Everything with portfolio
    path('add_portfolio', views.add_portfolio, name='add-portfolio'),
    path('list_portfolio', views.list_portfolio, name='list-portfolio'),
    path('show_portfolio/<portfolio_id>', views.show_portfolio, name='show-portfolio'),
    path('update_portfolio/<portfolio_id>', views.update_portfolio, name='update-portfolio'),
    path('delete_portfolio/<portfolio_id>', views.delete_portfolio, name='delete-portfolio'),
    path('portfolio_text', views.portfolio_text, name='portfolio-text'),
    path('portfolio_download_csv', views.portfolio_download_csv, name='portfolio-download-csv')
]
