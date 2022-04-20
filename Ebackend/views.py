from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login,logout, authenticate
from django.contrib import messages
from django.db import IntegrityError
from .models import VendorProfile, BuyerProfile, Product, Category
import os
from django.conf import settings
import django
import json
# index page--> accesible to all users (anonymous or not)
def index(request):
    user= request.user
    if request.method == 'GET':
        msg= messages.get_messages(request)
        products= Product.objects.all()#all products
        # get all categories to be passed into view dynamically:
        mattress= Category.productType.filter(category='mattress')
        living_room= Category.productType.filter(category='living')
        bed=Category.productType.filter(category='bed')

        context= {'msg': msg,
                  'name': user,
                  'products':products,
                  'mattress':mattress,
                  'living_room': living_room,
                  'bed': bed,
                    }
        return render(request, 'index.html', context)

def signup(request):
    if request.method == 'POST':
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
    # post method when vendor uploads a product
    if request.method == 'POST':
        print(request.POST)
        prodName= request.POST.get('product_name')
        prodDesc= request.POST.get('description')
        prodPrice= request.POST.get('product_price')
        category= request.POST.get('category')
        prodImg= request.FILES.get('product_image')
        # create product in the database, including its category if post data is sent.
        prod= Product.objects.create(vendor= user.vendorprofile, product_name=prodName, product_image=prodImg,description=prodDesc, price=prodPrice)
        Category.productType.create(product=prod, category=category)
        messages.success(request, 'Your product was successfully added, %s!' %user)
        return redirect('profile')
    # otherwise, get method for both vendor and buyer
    msg= messages.get_messages(request)
    context= {'msgs': msg,
              'name': user
                    }
    return render(request, 'profile.html', context)


# checkout page for registered buyers and non registered buyers
# expects only GET requests
def check_out(request):
    user= request.user
    # get all the data below, in case the product not in database.
    product_id= request.GET.get('product_id')
    product_name= request.GET.get('product_name')
    product_price=request.GET.get('price')
    # controls whether the page is requested through a product or directly with its url
    if product_id:
        # if the page requested through a product, split the img exention here. This to avoid attribute error(using 'split' method on None type) if not so.
        product_img_url= request.GET.get('product_img')
        # an exception handler in the case product not in the database
        try:
            request.session['my_product']= [product_name]
            product= Product.objects.get(product_name=product_name)
            return render(request, 'checkout.html', {'user':user,'product':product})
        except Product.DoesNotExist:
            # store product into session first, before storing to Product table
            request.session['my_product']= [product_name]
            try:
                product= Product.objects.create(buyer= user.buyerprofile, product_name= product_name, price= int(product_price), product_image=product_img_url)
                context= {'user': user,
                            'product' :product,
                            }
                return render(request, 'checkout.html', context)
            # catching an error, in case ther user is not a buyer or is an anonymous user(not signed up or logged in)
            except AttributeError or django.contrib.auth.models.User.buyerprofile.RelatedObjectDoesNotExist:
                # check if not anonymous (this means user is a vendor). Create a buyer profile for the vendor with its vendor details
                if isinstance(user, User):
                    bprof= BuyerProfile.objects.create(buyer=user, profile_img=user.vendorprofile.profile_img, phone= user.vendorprofile.phone, address= user.vendorprofile.address)
                    # now, store the product into the Product table with the vendor's BuyerProfile instance, which is 'bprof'
                    product= Product.objects.create(buyer= bprof, product_name= product_name, price= int(product_price), product_image=product_img_url)
                    context= {'user': user,
                            'product' :product,
                            }
                    return render(request, 'checkout.html', context)
                # otherwise, if user is anonmymous, display the product details without creating a profile.
                else:
                    product= Product.objects.create(product_name= product_name, price= int(product_price), product_image=product_img_url)
                    context= {
                            'product': product
                            }
                    return render(request, 'checkout.html', context)
    # this way, they used the checkout url directly or the upper "if condition" ran with neither success nor errors
    else:
        if request.session.get('my_product'):
            session_product= Product.objects.filter(product_name=request.session['my_product'][0])[0]
            return render(request, 'checkout.html',{'session_product':session_product})
        else:
            return render(request, 'checkout.html',{'no_item': 'No item in your cart'})

# endpoint to remover products--> reserved for only vendors 
@permission_required('Ebackend.can_edit_products', raise_exception=True)
def remove_prod(request):
    user= request.user
    prodId= int(request.GET.get('product_id'))
    print(prodId)
    Product.objects.get(id=prodId).delete()
    messages.info(request, 'product successfully removed from the database.')
    return redirect('profile')

def payment_method(request):
    pass

def add_to_cart(request):
    data= request.POST
    if data:
        print(data)
        return HttpResponse('items posted: %s' %data)

