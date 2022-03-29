from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    contact_number = models.CharField(unique=True, max_length=16)
    credit_card = models.CharField(null=True, unique=True, max_length=20)
    billing_address = models.CharField(unique=True, max_length=50)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + " " + str(self.username)

class Driver(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    contact_number = models.CharField(unique=True, max_length=16)
    credit_card = models.CharField(unique=True, max_length=20)
    billing_address = models.CharField(unique=True, max_length=50)
    vin_number = models.CharField(max_length=20, default=None)
    available = models.CharField(blank=False, max_length=20)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + self.first_name + ' ' + self.last_name

class Renter(models.Model):
    id = models.AutoField(primary_key=True)
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    email = models.EmailField(unique=True, max_length=50)
    contact_number = models.CharField(unique=True, max_length=16)
    credit_card = models.CharField(unique=True, max_length=20)
    billing_address = models.CharField(unique=True, max_length=50)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' ' + str(self.user_name)

class Equipment(models.Model):
    id = models.AutoField(primary_key=True)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    year = models.CharField(blank=False, max_length=4)
    brand_name = models.CharField(blank=False, max_length=20)
    model_name = models.CharField(blank=False, max_length=20)
    serial_number = models.CharField(unique=True, blank=False, max_length=20)
    current_location = models.CharField(max_length=50)
    daily_rate = models.CharField(blank=False, max_length=20)
    available = models.CharField(blank=False, max_length=20)
    registered = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' ' + self.year + ' ' + self.brand_name + ' ' + self.model_name + ' ' + str(self.renter)

class Order(models.Model):
    id = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    ordered = models.DateTimeField(auto_now_add=True)
    delivery_location = models.CharField(max_length=64)
    delivery_date = models.DateField(blank=True)
    return_date = models.DateField(blank=True)
    notes = models.CharField(max_length=100)

    def __str__(self):
        return 'Order: ' + str(self.id) + ' Location: '+ (self.delivery_location) + ' Equipment: ' + str(self.equipment) + ' Deliver: ' + str(self.delivery_date) + 'Return: ' + str(self.return_date) + ' Notes: ' + self.notes

class Contract(models.Model):
    id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    driver = models.ForeignKey(Driver, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    equipment = models.ForeignKey(Equipment, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    delivery_location = models.CharField(max_length=64)
    delivery_date = models.DateField(blank=True)
    return_date = models.DateField(blank=True)
    notes = models.CharField(max_length = 100)

    def __str__(self):
        return 'Contract: ' + str(self.id) + '  ' + str(self.order) + ' Created: ' + str(self.created)