from django.db import models
from django.shortcuts import redirect, render
from django.core.files.storage import FileSystemStorage
from .models import Search, Product

# Create your views here.

def home(request):
    return render(request, 'ecom_website/home.html')

def search(request):
    se = request.POST.get('search')
    if not se:
        se = ''

    results = Product.objects.filter(name__contains=se)
    
    p = {
        "results": results,
    }
    return render(request, 'ecom_website/search.html', p)

def details(request, pk):
    product = Product.objects.get(id=pk)
    front = {
        'prod':product,
        }

    return render(request, 'ecom_website/details.html', front)


def create(request):
    if request.method == "POST":
        name_post = request.POST.get('name')
        description_post = request.POST.get('description')
        price_post = request.POST.get('price')
        phone_post = request.POST.get('phone')
        category_post = request.POST.get('choice')
        owner_post = request.POST.get('owner')

        if request.POST.get('filename'):
            photo_post = request.FILES.getlist('photo')
            print(photo_post)
            for i in photo_post:
                photo_post = i
            Product.objects.create(name=name_post, price=price_post, description=description_post, owner=owner_post, primary_type=category_post, phone_number=phone_post, photo=photo_post)

        Product.objects.create(name=name_post, price=price_post, description=description_post, owner=owner_post, primary_type=category_post, phone_number=phone_post)
        return redirect('/search')
    
    

    
    return render(request, 'ecom_website/create.html')