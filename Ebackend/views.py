from email import message
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from .models import VendorProfile, BuyerProfile, Product

# Create your views here.

# index page--> accesible to all users (anonymous or not)
def index(request):
    user= request.user
    if request.method == 'GET':
        msg= messages.get_messages(request)
        context= {'msg': msg,
                  'name': user
                    }
        return render(request, 'index.html', context)

def signup(request):
    return render(request, 'signup.html', {})


def login_user(request):
    method = request.method
    post= request.POST
    get= request.GET
    if method == 'POST':
        username=post.get('username')
        password= post.get('password')
        user= authenticate(request, username= username, password=password)
        if user is not None:
            login(user)
            return redirect('/profile/')
        else:
            messages.error(request, 'username or password is incorrect!')
            return redirect('/login/')
    else:
        msg= messages.get_messages(request)
        return render(request, 'login.html', {'msgs': msg})
        

def logout_user(request):
    logout(request)

@login_required(login_url='/login/')
def profile(request):
    user= request.user
    msg= messages.get_messages(request)
    context= {'msg': msg,
              'name': user
                    }
    return render(request, 'profile.html', context)