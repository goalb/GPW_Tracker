from django import forms
from django.forms import ModelForm
from .models import Portfolio


#Create a portfolio form
class PortfolioForm(ModelForm):
    class Meta:
        model = Portfolio
        fields = "__all__" #Docelowa ma być --> ('name', 'company')

        labels = {
            'name': '',
            'company': '',
            'user': ''
        }

        widgets = {
            'name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Name'}),
            'company': forms.SelectMultiple(attrs={'class':'form-control', 'placeholder':'Company'}),
            'user': forms.TextInput(attrs={'class':'form-control', 'placeholder':'User'})
        }
