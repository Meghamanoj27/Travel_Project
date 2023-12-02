from django.contrib.auth.models import User
from django.contrib import messages, auth
from django.shortcuts import render, redirect



# Create your views here.


def login(request):
    if request.method == 'POST':
        USERNAME=request.POST['username']
        PASSWORD=request.POST['password']
        user=auth.authenticate(username=USERNAME,password=PASSWORD)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid user")
            return redirect('login')


    return render(request,'login.html')

def register (request):
    if request.method=='POST':
        USERNAME=request.POST['username']
        FIRSTNAME = request.POST['firstname']
        LASTNAME = request.POST['lastname']
        EMAIL = request.POST['email']
        PASSWORD = request.POST['password']
        CPASSWORD = request.POST['cpassword']
        if PASSWORD==CPASSWORD:
            if User.objects.filter(username=USERNAME).exists():
                messages.info(request,"USER NAME TAKEN")
                return redirect('register')
            elif User.objects.filter(email=EMAIL).exists():
                messages.info(request,"EMAIL ALREADY TAKEN")
                return redirect('register')
            else:
                user=User.objects.create_user(username=USERNAME,first_name=FIRSTNAME,last_name=LASTNAME,email=EMAIL, password =PASSWORD)
                user.save()
                # print("user registered")
                return redirect('login')
        else:
            messages.info(request,'password not match')
            return redirect('register')
        return redirect('/')
    return render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')




