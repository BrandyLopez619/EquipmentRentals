from django.shortcuts import render
from .models import Customer, Driver, Renter, Equipment, Order, Contract
# Create your views here.

def home(request):
    return render(request, 'home.html', {})


def customer(request):
    return render(request, 'customer.html', {})

def customer(request):
    all_customers = Customer.objects.all
    return render(request, 'customer.html', {'all':all_customers})  # {} is the context dictionary used to 

def driver(request):
    return render(request, 'customer.html', {})

def driver(request):
    all_drivers = Driver.objects.all
    return render(request, 'driver.html', {'all':all_drivers})  

def renter(request):
    return render(request, 'renter.html', {})

def renter(request):
    all_renters = Renter.objects.all
    return render(request, 'renter.html', {'all':all_renters})  

def equipment(request):
    return render(request, 'equipment.html', {})

def equipment(request):
    all_equipments = Equipment.objects.all
    return render(request, 'equipment.html', {'all':all_equipments})  

def order(request):
    return render(request, 'order.html', {})

def order(request):
    all_orders = Order.objects.all
    return render(request, 'order.html', {'all':all_orders})

def contract(request):
    return render(request, 'contract.html', {})

def contract(request):
    all_contracts = Contract.objects.all
    return render(request, 'contract.html', {'all':all_contracts})  