from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Orders, OrderUpdate
from math import ceil
import json


# Create your views here.
def index(request):

    allProds = []
    catprods = Product.objects.values("catagory", "id")
    cats = {item["catagory"] for item in catprods}
    for cat in cats:
        prod = Product.objects.filter(catagory=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    parms = {"allProds": allProds}
    return render(request, "shop/index.html", parms)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        phone = request.POST.get("phone", "")
        desc = request.POST.get("desc", "")
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
        thanks = True
        return render(request, "shop/contact.html", {"thanks": thanks})
    return render(request, "shop/contact.html")


def about(request):
    return render(request, "shop/about.html")


def tracker(request):
    if request.method == "POST":
        order_Id = request.POST.get("orderId", "")
        email = request.POST.get("email", "")

        try:
            order = Orders.objects.filter(Order_id=order_Id, email=email)

            if order.exists():
                update = OrderUpdate.objects.filter(order_id=order_Id)
                updates = []

                for item in update:
                    updates.append({
                        'text': item.update_desc,
                        'time': item.timestamp
                    })

                response = json.dumps([updates, order[0].items_json], default=str)
                return HttpResponse(response)

            else:
                return HttpResponse('No order found')

        except Exception as e:
            return HttpResponse(f'No order found')

    return render(request, "shop/tracker.html")


def search(request):
    return render(request, "shop/search.html")


def productviews(request, myid):
    # fetch the product using the id
    product = Product.objects.filter(id=myid)
    return render(request, "shop/productviews.html", {"product": product[0]})


def checkout(request):
    if request.method == "POST":
        items_json = request.POST.get("itemsJson", "")
        name = request.POST.get("name", "")
        email = request.POST.get("email", "")
        address = (
            request.POST.get("address1", "") + " " + request.POST.get("address2", "")
        )
        city = request.POST.get("city", "")
        state = request.POST.get("state", "")
        zip_code = request.POST.get("zip_code", "")
        phone = request.POST.get("phone", "")
        order = Orders(
            items_json=items_json,
            name=name,
            email=email,
            address=address,
            city=city,
            state=state,
            zip_code=zip_code,
            phone=phone,
        )
        order.save()
        update = OrderUpdate(order_id=order.Order_id, update_desc="The order has been placed")
        update.save()
        thanks = True
        id = order.Order_id
        return render(request, "shop/checkout.html", {"thanks": thanks, "id": id})
    return render(request, "shop/checkout.html")


def login(request):
    return render(request, "shop/login.html")


def cart(request):
    return render(request, "shop/cart.html")


def signup(request):
    return render(request, "shop/signup.html")
