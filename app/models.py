from django.db import models

# Create your models here.

class Car(models.Model):
    name = models.CharField(max_length=50)
    typename= models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    image = models.TextField()

    def __str__(self):
        return self.name
    
class Konfigurator(models.Model):
    car =  models.ForeignKey(Car, on_delete=models.CASCADE, related_name='konfiguratsiya') 
    konfiguratsiya = models.CharField(max_length=50)
    price = models.IntegerField()
    description = models.TextField()
    img = models.TextField()
    dvigatel = models.CharField(max_length=50)

    def __str__(self):
        return self.car.name