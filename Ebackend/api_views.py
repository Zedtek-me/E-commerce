from django.shortcuts import render, redirect
from Ebackend.serializers import VendorSerializer, BuyerSerializer, ProductSerializer
from Ebackend.models import BuyerProfile, VendorProfile,Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# getting all the vendors
@api_view(['GET'])
def get_vendor(request):
    vendors= VendorProfile.objects.all()
    Vserializer= VendorSerializer(vendors, many=True)
    return Response(Vserializer.data, status.HTTP_200_OK)

# getting all the buyers 
@api_view(['GET'])
def get_buyer(request):
    buyers= BuyerProfile.objects.all()
    Bserializer= BuyerSerializer(buyers, many=True)
    return Response(Bserializer.data, status.HTTP_200_OK)

# getting all the products
@api_view(['GET'])
def get_product(request):
    products= Product.objects.all()
    Pserializer= ProductSerializer(products, many=True)
    return Response(Pserializer.data, status.HTTP_200_OK)
