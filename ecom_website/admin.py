from django.contrib import admin
from django.db import models
from .models import Search, Product

# Register your models here.

admin.site.register(Search)
admin.site.register(Product)
