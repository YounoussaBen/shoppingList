from itertools import product
from django.shortcuts import render
from .models import Product

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'product': products})