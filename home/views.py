from django.shortcuts import render,HttpResponse,redirect
from home.models import Contact,bookr,register_customer
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from datetime import datetime
from django.contrib.auth.decorators import login_required
# Create your views here.

def signin(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("password")
        user=authenticate(request,username=username,password=password)
        if user is None:
           # return HttpResponse("fail")
            messages.warning(request, "Please Register First")
            return redirect("/signin")
        else:
            login(request,user)
            return render(request,"main.html")
            #return render(request,"start.html")
        
    return render(request,"start.html")
#    return HttpResponse("Hey ashim gautam")

def contact(request):
   if request.method=="POST":
    First=request.POST.get('First')
    
    email=request.POST.get('email')
    Message=request.POST.get('Message')
    contact=Contact(First=First,email=email,Message=Message) 
    contact.save()  
    messages.success(request, "Your Message has been sent.")
   return render(request,"contact.html")

def staffs(request):
    if request.user.is_anonymous:
        return redirect('/signin')
    return render(request,"staffs.html")

def main(request):
    return render(request,'main.html')

def register(request):
    if request.method=="POST":
        username=request.POST.get("username")
       # first=request.POST.get("ok")
        email=request.POST.get("email")
        password=request.POST.get("password")
        usern=User.objects.filter(username=username)
        if usern.exists():
            messages.warning(request, "Username is already taken")
        else:
            user=User(username=username,email=email)
            user.set_password(password)
            user.save()
            messages.success(request, "Your account has been created go to login page and login into your id")
        
    return render(request,'register.html')


def book(request):
    if request.method =='POST':
        firstname =request.POST.get('firstname')
        last =request.POST.get('last')
        email =request.POST.get('email')
        add =request.POST.get('add')
        city=request.POST.get('city')

        room =request.POST.get('room')
        phone =request.POST.get('phone')
        
        Book=bookr(firstname=firstname,last=last,email=email,add=add,city=city,room=room,phone=phone)
        
        Book.save() 
        messages.success(request, "You Room has been booked.You will be contact soon ")
        return render(request,'book.html')
        
    return render(request,'book.html')


@login_required(login_url="/signin")
def stafflog(request):
    if request.method=="POST":
        firstname=request.POST.get('firstname')
        last =request.POST.get('last')
        email =request.POST.get('email')
        add =request.POST.get('add')
        city=request.POST.get('city')
  #      date =request.POST.get('date')
        room =request.POST.get('room')
        phone =request.POST.get('phone')
        enterby=request.POST.get('enterby')
        customer=register_customer(firstname=firstname,last=last,email=email,add=add,city=city,room=room,phone=phone,enterby=enterby)

        customer.save()
        
    return render(request,"stafflog.html")


@login_required(login_url="/signin")
def customer_details(request):
    jquery=register_customer.objects.all()
    customerdata={'register_customer': jquery}
    return render(request,"viewcustomer.html",customerdata)


@login_required(login_url="/signin")
def delete_customer(request,id):
    jquery=register_customer.objects.get(id=id)
    jquery.delete()
    return redirect("/customerdetails")
    
def logoutu(request):
    logout(request,User)
    return render(request,"main.html")
