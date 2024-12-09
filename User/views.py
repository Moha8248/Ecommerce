from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Category

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'Home.html', {'categories': categories, 'products': products})
