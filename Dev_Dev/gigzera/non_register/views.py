from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact
from .forms import ContactForm

def index(request):
    return render(request, 'non_register/index.html')

def jobs(request):
    return render(request, 'non_register/jobs.html')

def aboutus(request):
    return render(request, 'non_register/aboutus.html')

def industries(request):
    return render(request, 'non_register/industries.html')

def findajob(request):
    return render(request, 'non_register/findajob.html')

def postajob(request):
    return render(request, 'non_register/postajob.html')

def signup(request):
    return render(request, 'non_register/signup.html')

def login(request):
    return render(request, 'non_register/login.html')

def forgot(request):
    return render(request, 'non_register/forgot.html')

# Contact form 
def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Your form has been submitted successfully!")
            return redirect('index')
        else:
            return messages.error(request, "Please fill out all fields!")
    return messages.error(request, "Invalid request!")
