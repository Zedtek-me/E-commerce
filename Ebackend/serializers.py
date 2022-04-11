from rest_framework import serializers
from .models import VendorProfile, BuyerProfile, Product, Category
from django.contrib.auth.models import User

class VendorSerializer(serializers.ModelSerializer):
    class Meta:
        model= VendorProfile
        field= '__all__'


class BuyerSerializer(serializers.ModelSerializer):
    class Meta:
        model= BuyerProfile
        field= '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        field= '__all__'


class CategorySerializers(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= '__all__'