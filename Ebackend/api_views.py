# from django.shortcuts import render, redirect
from Ebackend.serializers import VendorSerializer, BuyerSerializer, ProductSerializer, UserSerializer
from Ebackend.models import BuyerProfile, VendorProfile,Product
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User

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


@api_view(['GET', 'POST'])
def users(request):
    '''
    Create and Retrieves users per request.
    '''
    print(request.query_params)
    if request.method == 'POST':
        user_data= request.data
        serialized_user= UserSerializer(user_data)
        if serialized_user.is_valid():
            serialized_user.save()
            return Response(serialized_user.data, status.HTTP_201_CREATED)
    #otherwise, it's a get request; Now check if the request is meant for a single user or all users
    if not('pk' in request.query_params):
        '''This is a general get request-> returns all users'''
        query_set= User.objects.all()
        serialized_users= UserSerializer(query_set, many=True)
        return Response(serialized_users.data, status.HTTP_200_OK)
    else:#this means a single user is to be gotten
        pk= request.query_params.get('pk')
        user= User.objects.get(id=int(pk))
        serialized_user= UserSerializer(user)
        return Response(serialized_user.data, status.HTTP_200_OK)