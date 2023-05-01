from django.contrib import admin
from .models import (
    Car, 
    Konfigurator,
    Dilery,
    Extiyot_qisimlar,
    Sub_extiyotqisimlar,
    Cart,
    Cart_extiyotqisimlar,
    Order,
    Order_extiyotqisimlar,
    Like_Car,
    )

# Register your models here.

admin.site.register(Car)
admin.site.register(Konfigurator)
admin.site.register(Dilery)
admin.site.register(Extiyot_qisimlar)
admin.site.register(Sub_extiyotqisimlar)
admin.site.register(Cart)
admin.site.register(Cart_extiyotqisimlar)
admin.site.register(Order)
admin.site.register(Order_extiyotqisimlar)
admin.site.register(Like_Car)

