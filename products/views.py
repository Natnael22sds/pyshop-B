from django.http import HttpResponse
from django.shortcuts import render
from .models import Product


                                        # /products clall index
                                        #url resource locater (Adress)


def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products})


def new(request):
    return HttpResponse("It's Nati's project")
# Be ready for Monday
