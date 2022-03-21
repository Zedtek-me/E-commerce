from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import VendorProfile, BuyerProfile, Product

# Create your views here.

def index(request):
    if request.method == 'GET':
        msg= messages.get_messages(request)
        context= {'msg': msg}
        return render(request, 'index.html', context)

def signup(request):
    return render(request, 'signup.html', {})

def login(request):
    return render(request, 'login.html', {})