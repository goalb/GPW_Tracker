from django.db import models


# Create your models here.


class Company(models.Model):
    name = models.CharField('name', max_length=60)
    ticker = models.CharField('ticker', max_length=10)
    website = models.URLField('Website', max_length=100)

    def __str__(self):
        return self.name + ' (' + self.ticker + ')'


class User(models.Model):
    login = models.CharField('login', max_length=30)
    email = models.EmailField(max_length=200)
    name = models.CharField('name', max_length=60, null=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.login


class Portfolio(models.Model):
    name = models.CharField('name', max_length=60)
    company = models.ManyToManyField(Company, blank=True, null=True)
    user = models.IntegerField('portfolio user', blank=False, default=1)

    def __str__(self):
        return self.name
