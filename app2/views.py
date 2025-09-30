from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def mypage(request):
    return HttpResponse("heloooooo")

def mypage1(request):
    return render(request,"demo.html")
def index(request):
    return render(request,"index.html")
def ring(request):
    return render(request,"ring.html")
def neck(request):
    return render(request,"neck.html")
def ear(request):
    return render(request,"ear.html")
def products(request):
    return render(request,"products.html")
def product(request):
    return render(request,"product.html")
def bracelet(request):
    return render(request,"bracelet.html")
def contact(request):
    return render(request,"contact.html")
def about(request):
    return render(request,"about.html")

