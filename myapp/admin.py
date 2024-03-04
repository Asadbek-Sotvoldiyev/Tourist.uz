from django.contrib import admin
from .models import About, Category, Package

admin.site.register([About, Category, Package])
