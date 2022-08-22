from rest_framework import serializers
from Ebackend.models import VendorProfile, BuyerProfile, Product, Category
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializers):
    class Meta:
        model= User
        fields= ['name', 'username', 'email', 'is_staff', 'is_admin', 'is_superuser']

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= VendorProfile
        fields= '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model= BuyerProfile
        fields= '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields='__all__'

class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'