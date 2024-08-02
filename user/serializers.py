from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Product, Cart,Cart_items, Category

class LoginSerializer(serializers.Serializer):
    class Meta:
        models = User
        fields = ['username','password']

class AddCategoryserializer(serializers.Serializer):
    class Meta:
        models = Category
        fields = '__all__'

class AddProductSerializer(serializers.Serializer):
    class Meta:
        model = Product
        field = '__all__'

class ListProductSerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'


class CartSerializer(serializers.Serializer):
    class Meta:
        models = Cart
        fields = '__all__'

class AddCartItem(serializers.Serializer):
    class Meta:
        model = Cart_items
        fields = '__all__'

class ListCartItemsSerlizer(serializers.Serializer):
    cart = CartSerializer(read_only=True)
    product = ListProductSerializer(read_only=True)

    class Meta:
        models = Cart_items
        fields = ['cart','product']