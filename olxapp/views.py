from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import authenticate,login,logout
from . import forms
from django.contrib.auth.models import User
from django.contrib import messages
from olxapp.forms import ProductForm
from .models import Product,Cart,delivery
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe
from django.contrib.auth.decorators import login_required

#stripe.api_key=settings.STRIPE_SECRET_KEY

# Create your views here.
def home(request):
    furniture=Product.objects.filter(type='furniture')
    electronics=Product.objects.filter(type='electronics')
    Vehicles=Product.objects.filter(type='vehicles')
    #vehicles=Product.objects.get(type='Vehicles')
    #house=Product.objects.get(type='Vehicles')    
        
    return render(request,'home.html',{'furnitures': furniture,'electronics': electronics,'Vehicles':Vehicles})
 


def Registration(request):
    aj=forms.Register()
    if request.method =="POST":
            fm=forms.Register(request.POST)
            if fm.is_valid():
                fm.save()
                messages.success(request,'congragulation')
                return redirect('mylogin')
            else:
              return HttpResponse('soory')
    return render(request,'Registration.html',{'aj':aj})

def mylogin(request):
     fm=AuthenticationForm()
     if request.method == 'POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
         username=fm.cleaned_data['username']
         password=fm.cleaned_data['password']
         aj=authenticate(username=username,password=password)
         if aj is not None:
             login(request,aj)
             return redirect('home')
         else:
             pass
        
     return render(request,'login.html',{'aj':fm})


def sell(request):
     if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES) 
        print(form)
        if form.is_valid():
            name=form.cleaned_data['name']
            price=form.cleaned_data['price']
            address=form.cleaned_data['address']
            contact_no=form.cleaned_data['contact_no']
            image=form.cleaned_data['image']
            type=form.cleaned_data['type']
            print(name,price,address,contact_no)
            aj=Product(user=request.user,name=name.lower(),price=price,image=image,address=address,contact_no=contact_no,type=type.lower())
            aj.save()
            return redirect('home')
           #return redirect('home')  # Redirect to a product list page (you need to define this view)'''
        else:
            return HttpResponse('invalid')
     else:
        form = ProductForm()

     return render(request, 'sell.html', {'aj': form})

@login_required
def sellcart(request):
    cartproducts=Cart.objects.filter(user=request.user)
    myproduct=Product.objects.filter(user=request.user)      
    return render(request,'sellcart.html',{'mysellproducts':myproduct,'cartproducts':cartproducts})

@login_required
def addcart(request,id):
    aj=Product.objects.get(id=id)
    an=Cart(user=request.user,myid=aj)
    if an:
        an.save()
        return redirect('sellcart')
    else:
         return HttpResponse(id)
    
@login_required     
def deleted(request,id):
    sellpd=Product.objects.get(id=id)
    sellpd.delete()
    return redirect('sellcart')
@login_required
def deletecart(request,id):
    an=Cart.objects.filter(myid=id)
    for x in an:
        x.delete()
        return redirect('sellcart')

   
@login_required
def buy(request,id):
    product=Product.objects.filter(id=id)
    return render(request,'customerdetail.html',{'product':product})

@login_required
def ordered(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        address=request.POST['address']
        mobile=request.POST['phone']
        payment=request.POST['payment']
        if str(payment)!='credit':
            name=request.POST['name']
            email=request.POST['email']
            address=request.POST['address']
            mobile=request.POST['phone']
            payment=request.POST['payment']
            myid=request.POST['idname']
            pimage=Product.objects.get(id=myid)
            fm=delivery(user=request.user,name=name,email=email,address=address,mobile=mobile,payment=payment,orderid=pimage)
            if fm:
              fm.save()
              return redirect(checkout_session)
            else:
                pass
        else:
         id=request.POST['sessionToken']
         print(name,email,address,mobile,payment,id)
         pimage=Product.objects.get(id=id)
         fm=delivery(user=request.user,name=name,email=email,address=address,mobile=mobile,payment=payment,orderid=pimage)
         if fm:
            fm.save()
            return render(request,'odconformed.html')
         else:
             pass
        
    else:
        return HttpResponse('error 404')
@login_required
def orders(request):
    orderes=delivery.objects.filter(user=request.user)
    return render(request,'orders.html',{'orderes':orderes})


def mylogout(request):
    logout(request)
    return redirect('mylogin')


def search(request):
    if request.method =='POST':
        ans=request.POST['search']
        if ans.lower() == 'electronics':
              product=Product.objects.filter(type=ans.lower())
              return render(request,'searchproduct.html',{'products':product})
        elif ans.lower() == 'furniture' :
             product=Product.objects.filter(type=ans.lower())
             return render(request,'searchproduct.html',{'products':product})
        elif ans.lower() == 'vehicles' :
             product=Product.objects.filter(type=ans.lower())
             return render(request,'searchproduct.html',{'products':product})
        elif ans.lower() == 'house' :
             product=Product.objects.filter(type=ans.lower())
             return render(request,'searchproduct.html',{'products':product})
        else:
            product=Product.objects.filter(name=ans.lower())
            if product:
                      return render(request,'searchproduct.html',{'products':product})
            else:
                return HttpResponse('sotyu')

          
stripe.api_key='sk_test_51QRwkfFAlOtzX52InlvPwvW54gAceit98zj6wXqvfZLd3EklsKZoqbZjISwWL2tK3IJor8TcopmOIZfHbwPDgEMB00fMqV0Md6'

@login_required   
def checkout_session(request):
    checkout_session = stripe.checkout.Session.create(
                payment_method_types=['card'],
                line_items=[
                    {
                        'price_data': {
                            'currency': 'inr',
                            'product_data': {
                                'name': 't_shirt',
                                'name': 't_shirt',   # The product name
                            },
                            'unit_amount': 2000*100,  # Amount in cents ($20.00)
                        },
                        'quantity': 1,
                    },
                ],
                mode='payment',
                success_url=f'http://127.0.0.1:8000//success',
                cancel_url=f'http://127.0.0.1:8000//cancel',
            )

    return redirect(checkout_session.url, permanent=False)
 

@login_required   
def success(request):

        return render(request,'success.html')


@login_required
def cancel(request):
    return render(request,'cancel.html')



    

