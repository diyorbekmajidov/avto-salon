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

from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.hashers import make_password
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
    """
    url: http://car/delete/<int:pk>/
    delete car
    input: {
        "id": 1,
    }
    return: {
        "deleted": "deleted id: 1"
    }
    """
    def post(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            car.delete()
            return Response({'deleted': "deleted id: " + str(pk)})
        except ObjectDoesNotExist:
            return Response({'error': 'Car does not exist'})
class Carget(APIView):
    """
    url: http://car/<int:pk>/
    get car by id
    input: {
        "id": 1,
    }
    return: {
        "id": 1,
        "name": "BMW",
        "typename": "sedan",
        "model": "M5",
        "price": 100000,
        "description": "good car",
        "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bmw.com%2Fen%2Findex.html&psig=AOvVaw0QZ2Z4Q4Z2Q8ZQX6Z2Z2Z2&ust=1619786166262000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjQ4ZqH4_ACFQAAAAAdAAAAABAD"
    }
    """
    def get(self, request, pk):
        try:
            car = Car.objects.get(pk=pk)
            serializer = CarSerializer(car)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Car does not exist'})
        
class KonfiguratorViewSet(APIView):
    """
    url: http://konfigurator/
    create a new konfigurator
    input: {
        "name": "BMW",
        "typename": "sedan",
        "model": "M5",
        "price": 100000,
        "description": "good car",
        "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bmw.com%2Fen%2Findex.html&psig=AOvVaw0QZ2Z4Q4Z2Q8ZQX6Z2Z2Z2&ust=1619786166262000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjQ4ZqH4_ACFQAAAAAdAAAAABAD"
        car: 1
    }
    return: {
        "id": 1,
        "name": "BMW",
        "typename": "sedan",
        "model": "M5",
        "price": 100000,
        "description": "good car",
        "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bmw.com%2Fen%2Findex.html&psig=AOvVaw0QZ2Z4Q4Z2Q8ZQX6Z2Z2Z2&ust=1619786166262000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjQ4ZqH4_ACFQAAAAAdAAAAABAD"
        car: 1
    }

    """
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
        """
        url: http://konfigurator/<int:pk>/
        update konfigurator
        input: {
            "id": 1,
        }
        return: {
            "id": 1,
            "name": "BMW",
            "typename": "sedan",
            "model": "M5",
            "price": 100000,
            "description": "good car",
            "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bmw.com%2Fen%2Findex.html&psig=AOvVaw0QZ2Z4Q4Z2Q8ZQX6Z2Z2Z2&ust=1619786166262000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjQ4ZqH4_ACFQAAAAAdAAAAABAD"
            car: 1
        }
            """
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
    """
    url: http://konfigurator/delete/<int:pk>/
    delete konfigurator
    input: {
        "id": 1,
    }
    returns: {
        "deleted": "delet konfigurator by id: 1"
    }
    """
    def post(self, request, pk):
        try:
            konfigurator = Konfigurator.objects.get(pk=pk)
            konfigurator.delete()
            return Response({'deleted': True})
        except ObjectDoesNotExist:
            return Response({'error': 'Konfigurator does not exist'})
        
class Konfiguratorget(APIView):
    """
    url: http://http://127.0.0.1:8000/api/konfiguratorget/1/
    get car id all konfigurator
    input: {
        "id": 1,
    }
    returns: [{
        "id": 1,
        "car": 1,
        "name": "BMW",
        "typename": "sedan",
        "model": "M5",
        "price": 100000,
        "description": "good car",
        "image": "https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bmw.com%2Fen%2Findex.html&psig=AOvVaw0QZ2Z4Q4Z2Q8ZQX6Z2Z2Z2&ust=1619786166262000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjQ4ZqH4_ACFQAAAAAdAAAAABAD"
        }
    ]
    """
    def get(self, request, pk):
        arr=[]
        try:
            konfigurator = Konfigurator.objects.filter(car=pk)
            serializer = KonfiguratorSerializer(konfigurator, many=True)
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
        
class Extiyot_qisimlarView(APIView):
    """
    url: http://api/extiyot_qisimlar/
    create extiyot_qisimlar
    input: {
        "id": 1,
        "name": "tros",
        }
    return: {
        "id": 1,
        "name": "tros",
        }
    """
    def post(self, request):
        data = request.data
        serializer = PartsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

    def get(self, request):
        try:
            extiyot = Extiyot_qisimlar.objects.all()
            serializer = PartsSerializer(extiyot, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Extiyot does not exist'})
        
    def put(self, request, pk):
        try:
            extiyot = Extiyot_qisimlar.objects.get(pk=pk)
            serializer = PartsSerializer(instance=extiyot, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except ObjectDoesNotExist:
            return Response({'error': 'Extiyot does not exist'})


class Extiyot_qisimlardelete(APIView):
    """
    url: http://api/extiyot_qisimlardelete/1/
    delete extiyot_qisimlar
    input: {
        "id": 1,
        }
    return: {
        "deleted": "deleted id: 1"
        }
    """
    def post(self, request, pk):
        try:
            extiyot = Extiyot_qisimlar.objects.get(pk=pk)
            extiyot.delete()
            return Response({'deleted': "deleted id: " + str(pk)})
        except ObjectDoesNotExist:
            return Response({'error': 'Extiyot does not exist'})
        
class Sub_extiyotqisimlarView(APIView):
    def post(self, request):
        """
        url: http://api/sub_extiyotqisimlar/
        create sub_extiyotqisimlar
        input: {
            "id": 1,
            "name": "tros",
            "price": 10000,
            "description": "good",
            "img":"https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.bmw.com%2Fen%2Findex.html&psig=AOvVaw0QZ2Z4Q4Z2Q8ZQX6Z2Z2Z2&ust=1619786166262000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCJjQ4ZqH4_ACFQAAAAAdAAAAABAD",
            "extiyot_qisimlar": 1
            }

            """
        data = request.data
        serializer = Sub_SparepartsSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get(self, requset,id):
        arr=[]
        try:

            extiyot = Extiyot_qisimlar.objects.get(pk=id)
            sub_qisimlar=extiyot.sub_extiyot_qisimlar.all()
            serializer = Sub_SparepartsSerializer(sub_qisimlar,many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Extiyot does not exist'})

            
        
    def put(self, requset, pk):
        try:
            extiyot_qisimlar = Extiyot_qisimlar.objects.get(pk=pk)
            serializer = PartsSerializer(instance=extiyot_qisimlar, data=requset.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors)
        except ObjectDoesNotExist:
            return Response({'error': 'Extiyot does not exist'})
    
class Sub_extiyot_delet(APIView):
    def post(self, requset, pk):
        sub_extiyotqisim = Sub_extiyotqisimlar.objects.get(id=pk)
        sub_extiyotqisim.delete()
        return Response({"id":"delet by id"})
    
class Usercreateviews(APIView):
    def post(self,requset):
        data = requset.data
        username = data.get('username')
        password = data.get('password')
        if User.objects.filter(username = username):
            return Response({"return":"Such a user exists"})
        else:

            user = User.objects.create(username=username,password=password)
            token = Token.objects.create(user = user)
            return Response({'token':token.key})
        
class Userlogoutviews(APIView):
    def post(self,requset):
            """
    Logout a user
    input: https://api/logout/
    
    """
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        request.user.auth_token.delete()
        return Response({'success': 'Successfully logged out.'})
    
class Userloginviews(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        user = request.user
        token = Token.objects.get(user=user)
        if token:
            token.delete()
        token= Token.objects.create(user=user)
        return Response({"token":token.key})
        
class CartView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request):
        data = request.data
        data['user'] = request.user.id
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    def get(self, request):
        try:
            user=request.user
            cart = Cart.objects.filter(user=user)
            serializer = CartSerializer(cart, many=True)
            return Response(serializer.data)
        except ObjectDoesNotExist:
            return Response({'error': 'Cart does not exist'})
        
class Cartdelete(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self, request, pk):
        try:
            user = request.user
            cart  = Cart.objects.filter(user=user,id=pk)
            cart.delete()
            return Response({'deleted': "deleted id: "})
        except ObjectDoesNotExist:
            return Response({'error': 'Cart does not exist'})
