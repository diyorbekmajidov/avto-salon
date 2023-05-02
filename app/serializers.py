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
    sub_car = KonfiguratorSerializer(many=True, read_only=True)
    class Meta:
        model = Car
        fields = '__all__'

class DilerySerializer(serializers.ModelSerializer):
    class Meta:
        model = Dilery
        fields = '__all__'

