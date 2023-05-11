from django.db import models
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50)
    typename= models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name
    
class Konfigurator(models.Model):
    car =  models.ForeignKey(Car, on_delete=models.CASCADE, related_name='konfiguratsiya') 
    konfiguratsiya = models.CharField(max_length=50)
    price = models.FloatField()
    description = models.TextField()
    img = models.TextField()
    dvigatel = models.CharField(max_length=50)

    def __str__(self):
        return self.car.name
    
class Dilery(models.Model):
    name= models.CharField(max_length=50)
    phone_number = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):  
        return self.name
    
class Extiyot_qisimlar(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Sub_extiyotqisimlar(models.Model):
    extiyot_qisimlar = models.ForeignKey(Extiyot_qisimlar, on_delete=models.CASCADE, related_name='sub_extiyot_qisimlar')
    name = models.CharField(max_length=50)
    description = models.TextField()
    img = models.TextField()

    def __str__(self):
        return self.extiyot_qisimlar.name

class Cart(models.Model):
    user = models.ForeignKey(User, related_name='cart',on_delete=models.CASCADE)
    konfiguratsiya = models.ForeignKey(Konfigurator, on_delete=models.CASCADE, related_name='cart')
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.username
    
class Cart_extiyotqisimlar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cart_extiyotqisimlar')
    sub_extiyotqisimlar = models.ForeignKey(Sub_extiyotqisimlar, on_delete=models.CASCADE, related_name='cart_extiyotqisimlar')
    quantity = models.IntegerField()

    def __str__(self):
        return self.user.username
    
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='order')
    konfiguratsiya = models.ForeignKey(Konfigurator, on_delete=models.CASCADE, related_name='order')
    phone_number = models.CharField(max_length=50)
    total_price = models.FloatField()

    def __str__(self):
        return self.user.username
    
class Order_extiyotqisimlar(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Order_extiyotqisimlar')
    sub_extiyotqisimlar = models.ForeignKey(Sub_extiyotqisimlar, on_delete=models.CASCADE, related_name='order_extiyotqisimlar')
    phone_number = models.CharField(max_length=50)
    total_price = models.FloatField()

    def __str__(self):
        return self.user.username
    
class Like_Car(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like_car')
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='like_car')

    def __str__(self):
        return self.user.username