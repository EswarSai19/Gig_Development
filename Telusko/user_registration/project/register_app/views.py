from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request, 'register_app/home.html')

def register(request):
    if request.method == "POST":
        fn = request.POST['first_name']
        un = request.POST['user_name']
        ln = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']

        if User.objects.filter(username=un).exists():
            messages.info(request, "username already exists")
            return redirect('register')

        elif User.objects.filter(email=email).exists():
            messages.info(request, "Email already exists")
            return redirect('register')
        else:
            user = User.objects.create_user(username=un, first_name=fn, last_name=ln, email=email, password=password)
            user.save();
            messages.info(request, "User created")
            return redirect('home')
    else:
        return render(request, 'register_app/register.html')