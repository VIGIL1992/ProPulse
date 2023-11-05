from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db.models import Q

# Create your views here.

# This function will take to home page
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    
    
    
    context = {
        'categories' : categories,
        'products'  : products,
    }
    # return render(request, 'index.html',{})
    return render(request, 'home.html', context)


# This function will take to product page
def products(request,category_slug=None):
    products = Product.objects.all()
    categories = Category.objects.all()
    
    context = {
        'categories' : categories,
        'products'  : products,
    }
    return render(request, 'products.html', context)


# This function is for search function and take us to store page
def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('product_name').filter(Q(description__icontains=keyword) | Q(product_name__icontains=keyword))
            

    context = {
        'products' : products,

    }
    return render(request, 'products.html',context)


def about_us(request):
    
    
    return render(request, 'about_us.html'    )


def contact_us(request):
    
    
    return render(request, 'contact_us.html'    )


