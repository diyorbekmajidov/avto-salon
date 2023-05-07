from rest_framework import serializers
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
    )


    
class KonfiguratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konfigurator
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class DilerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dilery
        fields = '__all__'

class PartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Extiyot_qisimlar
        fields = '__all__'

class Sub_SparepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sub_extiyotqisimlar
        fields = '__all__'

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = '__all__'

class Cart_SparepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_extiyotqisimlar
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class Order_SparepartsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order_extiyotqisimlar
        fields = '__all__'


