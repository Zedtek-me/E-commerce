# from django.shortcuts import render, redirect
from Ebackend.serializers import VendorSerializer, BuyerSerializer, ProductSerializer
from Ebackend.models import BuyerProfile, VendorProfile,Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# getting all the vendors
@api_view(['POST','GET'])
def get_vendor(request):
    if request.method == 'POST':
        posted_data= request.data
        serialized_data= VendorSerializer(posted_data)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else: 
            return Response({'invalid_data':'data you provided was not correct!'}, status=status.HTTP_406_NOT_ACCEPTABLE)
    else:
        if (request.query_params and 'pk' in request.query_params):
            pk= request.query_params.get('pk', 1)
            individual_user= VendorProfile.objects.get(id=pk)#gets the individual vendor alone, not all
            serialized_user= VendorSerializer(individual_user)
            return Response(serialized_user.data, status.HTTP_200_OK)
        vendors= VendorProfile.objects.all()
        Vserializer= VendorSerializer(vendors, many=True)
    return Response(Vserializer.data, status.HTTP_200_OK)

# getting all the buyers 
@api_view(['POST','GET'])
def get_buyer(request):
    buyers= BuyerProfile.objects.all()
    Bserializer= BuyerSerializer(buyers, many=True)
    return Response(Bserializer.data, status.HTTP_200_OK)

# getting all the products
@api_view(['POST','GET'])
def get_product(request):
    products= Product.objects.all()
    Pserializer= ProductSerializer(products, many=True)
    return Response(Pserializer.data, status.HTTP_200_OK)
