from multiprocessing import AuthenticationError
from django.shortcuts import redirect, render
from . models import place,icon
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import messages,auth
# Create your views here.
def demo(request):
    obj=place.objects.all()
    obj1 = icon.objects.all()    
    return render(request, 'index.html', {'result': obj, 'icons': obj1})
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('demo')
        else:
            messages.info(request,"invalid credentials")
            return redirect('login')
    return render(request,'login.html')
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['first_name']
        email=request.POST['email']
        password=request.POST['password']
        password1=request.POST['password1']
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username exists')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email exists')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password,first_name=first_name,email=email) 
                user.save();
                return redirect('login')
        else:
            messages.info(request,"password not matching")
            return redirect('register')
        return redirect('demo')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('demo')