from rest_framework import serializers
from .models import Car, Konfigurator


    
class KonfiguratorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Konfigurator
        fields = '__all__'

class CarSerializer(serializers.ModelSerializer):
    sub_car = KonfiguratorSerializer(many=True, read_only=True, related_name='car')
    class Meta:
        model = Car
        fields = '__all__'