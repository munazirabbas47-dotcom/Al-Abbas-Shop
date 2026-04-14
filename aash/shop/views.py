from django.shortcuts import render
from django.http import HttpResponse
from .models import Product,Contact
from math import ceil

# Create your views here.
def index(request):
    # products = Product.objects.all()
    # print(products)
    # n = len(products)
    # nSlides = n//4 + ceil((n/4)-(n//4))
    # parms = {'numberofSlides': nSlide , 'range' : range(1,nSlide) , 'product' : products}
    # allProds = [[products, range(1 , nSlides), nSlides],[products, range(1 , nSlides) , nSlides]]

    allProds = []
    catprods = Product.objects.values('catagory', 'id')
    cats = {item['catagory']  for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n//4 + ceil((n/4)-(n//4))
        allProds.append([prod,range(1,nSlides), nSlides])

    parms = {'allProds' : allProds}
    return render(request, "shop/index.html",parms)


def contact(request):
    if request.method=="POST":
        name = request.POST.get('name','')
        email = request.POST.get('email','')
        phone = request.POST.get('phone','')
        desc = request.POST.get('desc', '')
        # print(name,email,phone,desc)
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
    return render(request, "shop/contact.html")

def about(request):
    return render(request, "shop/about.html") 

def tracker(request):
    return render(request, "shop/tracker.html")

def search(request):
    return render(request, "shop/search.html")

def productviews(request,myid):
    # fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, "shop/productviews.html",{'product':product[0]})

def checkout(request):
    return render(request, "shop/checkout.html")

def login(request):
    return render(request, "shop/login.html")


def cart(request):
    return render(request, "shop/cart.html")

def signup(request):
    return render(request, "shop/signup.html")