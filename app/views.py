from django.shortcuts import render
from .models import Car, Konfigurator
from .serializers import CarSerializer, KonfiguratorSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from django.core.exceptions import ObjectDoesNotExist



class CarViewSet(APIView):
    def post(self, request):
        data = request.data
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
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