from django.http import HttpResponse
from django.shortcuts import render
from .models import Products # .models current folder

# Create your views here.
def index(request):
    products = Products.objects.all() # returns all
    # return HttpResponse("Hello World")
    return render(request, 'index.html', {'products':products})

def new(request):
    return HttpResponse("New Products")