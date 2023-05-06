from django.shortcuts import render
from .models import (
    Car, 
    Konfigurator,
    Dilery,
    Extiyot_qisimlar,
    Sub_extiyotqisimlar,
    Cart,
    Order,
    Cart_extiyotqisimlar,
    Order_extiyotqisimlar,

    )
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist
from .serializers import (
    CarSerializer, 
    KonfiguratorSerializer,
    DilerySerializer,
    PartsSerializer,
    Sub_SparepartsSerializer,
    CartSerializer,
    Cart_SparepartsSerializer,
    OrderSerializer,
    Order_SparepartsSerializer,
)



class CarViewSet(APIView):
    """
    url: http://127.0.0.1:8000/api/car/
    create a new car
    input: {
        "name": "BMW",
        "typename": "sedan",
        "model": "M5",
        "price": 100000,
        "description": "good car",
        "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bmw.com%2Fen%2Findex.html&psig=AOvVaw0QZ2Z4Q4Z2Q8ZQX6Z2Z2Z2&ust=1619786166262000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjQ4ZqH4_ACFQAAAAAdAAAAABAD"
    }

    """
    def post(self, request):
        data = request.data
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        """
        get all cars
        url:http://127.0.0.1:8000/
        rerurns: {
            "id": 1,
            "name": "BMW",
            "typename": "sedan",
            "model": "M5",
            "price": 100000,
            "description": "good car",
            "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bmw.com%2Fen%2Findex.html&psig=AOvVaw0QZ2Z4Q4Z2Q8ZQX6Z2Z2Z2&ust=1619786166262000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjQ4ZqH4_ACFQAAAAAdAAAAABAD"
        }
        """
        try:
            car = Car.objects.all()
            serializer = CarSerializer(car, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Car does not exist'})
        
    def put(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(instance=car, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except ObjectDoesNotExist:
            return Response({'error': 'Car does not exist'})
        
class CarViewdelete(APIView):
    def post(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return Response({'deleted': "deleted id: " + str(pk)})
        except ObjectDoesNotExist:
            return Response({'error': 'Car does not exist'})
        
class KonfiguratorViewSet(APIView):
    def post(self, request):
        data = request.data
        serializer = KonfiguratorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        try:
            konfigurator = Konfigurator.objects.all()
            serializer = KonfiguratorSerializer(konfigurator, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Konfigurator does not exist'})
        
    def put(self, request, pk):
        try:
            konfigurator = Konfigurator.objects.get(pk=pk)
            serializer = KonfiguratorSerializer(instance=konfigurator, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except ObjectDoesNotExist:
            return Response({'error': 'Konfigurator does not exist'})

class Konfiguratordelete(APIView):    
    def post(self, request, pk):
        try:
            konfigurator = Konfigurator.objects.get(pk=pk)
            konfigurator.delete()
            return Response({'deleted': True})
        except ObjectDoesNotExist:
            return Response({'error': 'Konfigurator does not exist'})
        
class Konfiguratorget(APIView):
    def get(self, request, pk):
        try:
            name = Konfigurator.objects.filter(id=pk)
            serializer = KonfiguratorSerializer(name, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Konfigurator does not exist'})

class DileryViewSet(APIView):
    def post(self, request):
        data = request.data
        serializer = DilerySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        try:
            dilery = Dilery.objects.all()
            serializer = DilerySerializer(dilery, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Dilery does not exist'})
        
    def put(self, request, pk):
        try:
            dilery = Dilery.objects.get(pk=pk)
            serializer = DilerySerializer(instance=dilery, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except ObjectDoesNotExist:
            return Response({'error': 'Dilery does not exist'})
        
class Dilerydelete(APIView):
    def post(self,request, pk):
        try:
            dilery = Dilery.objects.get(pk=pk)
            dilery.delete()
            return Response({'deleted': "deleted id: " + str(pk)})
        except ObjectDoesNotExist:
            return Response({'error': 'Dilery does not exist'})


        