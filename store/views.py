from django.shortcuts import render
from .models import Category, Product

# Create your views here.

def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    
    
    context = {
        'categories' : categories,
        'products'  : products,
    }
    # return render(request, 'index.html',{})
    return render(request, 'home.html', context)


def products(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    context = {
        'categories' : categories,
        'products'  : products,
    }
    return render(request, 'products.html', context)


def about_us(request):
    
    
    return render(request, 'about_us.html'    )


def contact_us(request):
    
    
    return render(request, 'contact_us.html'    )