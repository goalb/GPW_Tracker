from django import forms
from django.forms import ModelForm
from .models import Portfolio


# Create a portfolio form as user
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = ('name', 'company')

        labels = {
            'name': '',
            'company': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'company': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder':'Company'}),
        }


# Create a portfolio form as admin
class PortfolioFormAdmin(ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__"

        labels = {
            'name': '',
            'company': '',
            'user': '',
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder':'Name'}),
            'company': forms.SelectMultiple(attrs={'class': 'form-control', 'placeholder':'Company'}),
        }