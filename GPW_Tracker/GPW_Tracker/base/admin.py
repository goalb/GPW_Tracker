from django.contrib import admin
from .models import Company
from .models import User
from .models import Portfolio

# Register your models here.
admin.site.register(Company)
admin.site.register(User)
admin.site.register(Portfolio)

