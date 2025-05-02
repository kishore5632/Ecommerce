from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.models import User
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import *
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.db.models import Min,Max
from django.core.paginator import Paginator,EmptyPage

def index(request):
    product=Product.objects.filter(category_id = 1 ).order_by('-timestamp')[:6]
    context = {'mens': product}  
    return render(request,"index.html",context)

def Register(request):
    if request.method == 'POST':
        if 'login' in request.POST:
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(username=username,password=password)
            if user is not None:
                login(request,user)
                messages.success(request,"login success")
            else:
                messages.warning(request,'Username or password is incorrect')
    
        elif 'register' in request.POST:
                    
            fname = request.POST["firstname"]
            lname = request.POST["lastname"]
            pwd =  request.POST["password"]
            cpwd = request.POST["confirm_password"]
            uname = request.POST["username"]
            em = request.POST["email"]
            if (pwd == cpwd):
                data = User.objects.create_user(first_name=fname,last_name=lname,username=uname,email= em,password=pwd)
                d = register()
                d.user = data
                d.save()
                messages.success(request,"You're Registered Successfully")
            else:
               messages.warning(request,"password and confirm password are not same!")

    return render(request,'account.html')

def user(request):
    user = request.user
    return render(request,'logout.html',{'user':user})

def user_logout(request):
    logout(request)
    return redirect("index")

def blog_archives(request):
    posts = Poster.objects.all()
    latest = Poster.objects.order_by('-timestamp')[:3]
    context = {'posts':posts,'late':latest}
    return render(request,"blog-archive.html",context)

def blog_single(request,id):
    posts = Poster.objects.filter(id=id)
    nextpost = Poster.objects.filter().order_by('id').first()
    prevpost = Poster.objects.filter().order_by('id').last()    
    
    post = Comment.objects.filter(post_id=id)

    if request.method == 'POST':
        n = request.POST["name"]
        em = request.POST["email"]
        com = request.POST["comment"]
        cs = Comment(Name=n,email=em,content=com)
        cs.post = Poster.objects.filter(id=id).first()
        cs.save()
        messages.success(request,"Thanks For Your comment") 
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
          
    context = {'posts': posts,'nextpost':nextpost,'prevpost':prevpost,'post':post}
    return render(request,'blog-single.html',context)

# def comm(request):
#      if request.method == 'POST':
#         N = request.POST["name"]
#         em = request.POST["email"]
#         com = request.POST["comment"]
#         cs = Comment(Name=N,email=em,content=com)
#         cs.save()
#         return HttpResponse('your saved successfully')
#      return render(request,"post.html")

def add_cart(request,product_id):
   product = Product.objects.get(id=product_id)
   cart, created = Cart.objects.get_or_create(user=request.user,complete=True)

   try:
       carts = cart_items.objects.get(cart=cart,product=product)
       if carts.quantity <  carts.product.stock:
             carts.quantity +=1
       carts.save()

   except:
       carts = cart_items.objects.create(product=product,quantity=1,cart=cart)
       carts.save()
    
   return redirect('cart_detail')

def cart_detail(request,total=0,counter=0):
   try: 
    cart, created = Cart.objects.get_or_create(user=request.user,complete=True)
    cart_item =cart_items.objects.filter(cart=cart,active=True)
    for  cart in cart_item:
        total =total + (cart.product.price * cart.quantity)
        counter += cart.quantity

   except ObjectDoesNotExist:
        pass
   
   context = {'cart_item':cart_item,'total':total,'counter':counter} 
  
   return render(request,'cart.html',context)

def complete_remove(request,product_id):
    cart, created = Cart.objects.get_or_create(user=request.user,complete=True)
    cart_item = cart_items.objects.get(product_id=product_id,cart=cart)
    cart_item.delete()
    return redirect('cart_detail')

def remove_quantity(request,product_id):
    cart, created = Cart.objects.get_or_create(user=request.user,complete=True)
    cart_item = cart_items.objects.get(product_id=product_id,cart=cart) 
    if cart_item.quantity > 1:
        cart_item.quantity-=1
        cart_item.save()
    else:
        cart_item.delete()
    
    return redirect('cart_detail')

def checkout(request,total=0,counter=0):
   try: 
        cart, created = Cart.objects.get_or_create(user=request.user,complete=True)
        cart_item =cart_items.objects.filter(cart=cart,active=True)
        for  cart in cart_item:
            total =total + (cart.product.price * cart.quantity)
            counter += cart.quantity

   except ObjectDoesNotExist:
        pass
   
   context = {'cart_item':cart_item,'total':total,'counter':counter} 
  
   return render(request,'checkout.html',context)



def product(request):
    try:
        product=Product.objects.all()
        paginator = Paginator(product, 5) # Show 5 contacts per page.
        page_number = request.GET.get('page',1)
        try:            
            page_obj = paginator.page(page_number)
        except EmptyPage:
            page_obj = paginator.page(1)

    except:
        cart, created  = Cart.objects.get_or_create(user=request.user,complete=True)
        product = Wishlist.objects.filter(cart=cart)
   
    context = {'pros': page_obj}
    return render(request,'product.html',context)


def Men(request,category_id):
    try:
        product=Product.objects.filter(category_id=1)
    except:
        cart, created  = Cart.objects.get_or_create(user=request.user,complete=True)
        product = Wishlist.objects.filter(cart=cart)
    
    #price = Product.objects.aggregate(Min('price'),Max('price'))
    context = {'mens': product}
    return render(request,'mens.html',context)



def Women(request,category_id):
    try:
        product=Product.objects.filter(category_id=2)
    except:
        cart, created  = Cart.objects.get_or_create(user=request.user,complete=True)
        product = Wishlist.objects.filter(cart=cart)
    
    context = {'womens': product}
    return render(request,'womens.html',context)

def Furniture(request,category_id):
    try:
        product=Product.objects.filter(category_id=3)
    except:
        cart, created  = Cart.objects.get_or_create(user=request.user,complete=True)
        product = Wishlist.objects.filter(cart=cart)
    
    context = {'furniture': product}
    return render(request,'furniture.html',context)


def sports(request,category_id):
    try:
        product=Product.objects.filter(category_id=4)
    
    except:
        cart, created  = Cart.objects.get_or_create(user=request.user,complete=True)
        product = Wishlist.objects.filter(cart=cart)
    context = {'sports': product}
    return render(request,'sports.html',context)

def electronics(request,category_id):
    try:
       product=Product.objects.filter(category_id=5)

    except:
        cart, created  = Cart.objects.get_or_create(user=request.user,complete=True)
        product = Wishlist.objects.filter(cart=cart)
    context = {'electronics': product}
    return render(request,'electronics.html',context)


def wishlist(request,product_id):
   product = Product.objects.get(id=product_id)
   cart, created = Cart.objects.get_or_create(user=request.user,complete=True)

   try:
       carts = Wishlist.objects.get(product=product,cart=cart)
       carts.save()

   except:
       carts = Wishlist.objects.create(product=product,cart=cart)
       carts.save()

   return redirect('wishlist_detail')

def wishlist_detail(request):
   try:
        cart, created = Cart.objects.get_or_create(user=request.user,complete=True)
        carts = Wishlist.objects.filter(cart=cart)

   except ObjectDoesNotExist:
        pass
   
   return render(request,'wishlist.html',{'carts':carts})

def complete_remove_wishlist(request,product_id):
    cart, created = Cart.objects.get_or_create(user=request.user,complete=True)
    cart_item = Wishlist.objects.get(product_id=product_id,cart=cart)
    cart_item.delete()
    return redirect('wishlist_detail')



#this is demo

#This is demo for testing...
#this is for demo (Edited by-Ambar Kaity)