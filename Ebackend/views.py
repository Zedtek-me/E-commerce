from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.db import IntegrityError
from .models import VendorProfile, BuyerProfile, Product

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
    if request.method == 'POST':
        print(request.POST)
        name= request.POST.get('name')
        email= request.POST.get('email')
        username= request.POST.get('username')
        typeof_user= request.POST.get('usertype')
        password= request.POST.get('password')
        password2= request.POST.get('password2')

        # check whether passwords correspond. If so, check whether name is not taken
        if password == password2:
            try:
                user= User.objects.create_user(first_name= name, username=username, password=password, email=email)
            except IntegrityError:
                messages.error(request, 'Username is already taken!')
                return redirect('/signup/')
            # check which user it is (buyer or seller)
            if typeof_user == 'buyer':
                buyer= BuyerProfile(buyer= user)
                buyer.save()
                messages.success(request, 'account successfully created!')
                return redirect('/login/')
            vendor= VendorProfile(vendor= user)
            vendor.save()
            messages.success(request, 'account successfully created!')
            return redirect('/login/')
        # return error if passwords don't match
        messages.error(request, 'Your passwords didn\'t match!')
        return redirect('/signup/')
    msgs= messages.get_messages(request)
    return render(request, 'signup.html', {'msgs': msgs})


def login_user(request):
    method = request.method
    post= request.POST
    get= request.GET
    if method == 'POST':
        username=post.get('username')
        password= post.get('password')
        user= authenticate(request, username= username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(0)
            return redirect('/profile/')
        else:
            messages.error(request, 'username or password is incorrect!')
            return redirect('/login/')
    else:
        msgs= messages.get_messages(request)
        return render(request, 'login.html', {'msgs': msgs})
        

def logout_user(request):
    logout(request)
    return redirect('/login/')

# profile page for both buyers and sellers
@login_required(login_url='/login/')
def profile(request):
    user= request.user
    print(request.session.items())
    msg= messages.get_messages(request)
    context= {'msg': msg,
              'name': user
                    }
    return render(request, 'profile.html', context)


# checkout page for registered buyers and non registered buyers
# expects only GET requests
def check_out(request):
    user= request.user
    product_id= int(request.GET['product_id'])
    # get all the data below, in case the product not in database.
    product_name= request.GET['product_name']
    product_price=int(request.GET['price'])
    try:
        if user.is_authenticated and user.buyerprofile.buyer:
            try:
                product= Product.objects.get(id=product_id)
                return render(request, 'checkout.html', {'user':user,'product':product})
            except Product.DoesNotExist:
                request.session['my_product']= [product_name]
                product= Product.objects.create(buyer= user.buyerprofile, product_name= product_name, price= product_price)
                context={'user': user,'product': product}
                return render(request, 'checkout.html', context)
        
        elif not user.is_authenticated:
            context= {'user':user, 
                    'product_price': product_price,
                    'product_name': product_name,
                    }
            return render(request, 'checkout.html',context)
    except Exception as err:
        print(user.buyerprofile.buyer)
        return HttpResponse(err)