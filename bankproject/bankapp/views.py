from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib import messages,auth

# Create your views here.
def index(request):
    return render(request,'main.html')

def login(request):
    if request.method == 'POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('form')
        else:
            messages.info(request,'Check Credentials')
            return redirect('login')
    return render(request,'login.html')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request, 'Passwords not match')
            return redirect('register')
        return redirect('/')

    return render(request, 'register.html')

def form(request):
    if request.method == 'POST':
        name=request.POST['name']
        dob=request.POST['dob']
        age=request.POST['age']
        gender=request.POST['gender']
        phonenumber=request.POST['phonenumber']
        mailid=request.POST['mailid']
        address=request.POST['address']
        return redirect('/')
    return render(request, 'form.html')

def logout(request):
    auth.logout(request)
    return redirect('/')