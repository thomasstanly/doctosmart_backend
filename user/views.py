from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import  viewsets
from rest_framework.generics import ListCreateAPIView
from .serializers import LoginSerializer
from .models import Product,Cart,Cart_items,Category
# Create your views here.

class Login(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = LoginSerializer

class Product(ListCreateAPIView):
    queryset = Product.objects.all()
    
    def get(self, request):
        pass
    def post(self, request):
        pass
    