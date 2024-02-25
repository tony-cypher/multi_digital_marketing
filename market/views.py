from django.shortcuts import render
from django.http import JsonResponse, HttpResponseNotFound
from .models import Product, Order
import json

# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'market/index.html', {'products':products})


def detail(request, id):
    product = Product.objects.get(id=id)
    return render(request, 'market/detail.html', {'product':product})

def crate_checkout(request, id):
    request_data = json.load(request.body)
    product = Product.objects.get(id=id)
    order = Order()
    order.customer_email = request_data['email']
    order.product = product
    order.payment_intent = 'Successfuly paid'
    order.amount = int(Product.price)
    order.save()

    return JsonResponse({'session_id':200})