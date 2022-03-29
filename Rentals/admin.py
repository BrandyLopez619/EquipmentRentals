from django.contrib import admin
from .models import Customer, Driver, Renter, Equipment, Order, Contract
# Register your models here.

admin.site.register(Customer)
admin.site.register(Driver)
admin.site.register(Renter)
admin.site.register(Equipment)
admin.site.register(Order)
admin.site.register(Contract)