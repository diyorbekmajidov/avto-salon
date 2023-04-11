from rest_framework import serializers
from .models import Car, Konfigurator

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'
    
class KonfiguratorSerializer(serializers.ModelSerializer):
    sub_car = CarSerializer(many=True, read_only=True)
    class Meta:
        model = Konfigurator
        fields = '__all__'