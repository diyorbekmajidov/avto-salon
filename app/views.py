from django.shortcuts import render
from .models import Car, Konfigurator
from .serializers import CarSerializer, KonfiguratorSerializer
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView


class CarViewSet(APIView):
    def post(self, request):
        data = request.data
        serializer = CarSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.data)
