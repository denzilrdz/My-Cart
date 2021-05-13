from django.shortcuts import render
from django.http import HttpResponse
from .models import Product
from math import ceil

# Create your views here.

def index(request):
    #products = Product.objects.all()
    #params = {'products':products, 'no_of_slides':nSlides, 'range':range(1,nSlides)}
    #allProducts = [[products, range(1,nSlides), nSlides],
    #[products, range(1,nSlides), nSlides]]
    allProducts = []
    catProd = Product.objects.values('category','id')
    cats = {item['category'] for item in catProd}
    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProducts.append([prod, range(1, nSlides), nSlides])
    params = {'allProducts':allProducts}
    return render(request, 'shop/index.html', params)

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return HttpResponse("Contact Page")

def tracker(request):
    return HttpResponse("Tracker Page")

def search(request):
    return HttpResponse("Search Page")

def productView(request):
    return HttpResponse("Product View Page")

def checkOut(request):
    return HttpResponse("Chekout Page")