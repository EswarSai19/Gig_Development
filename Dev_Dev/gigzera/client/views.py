

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact, Client
from .forms import ContactForm

# Create your views here.
# Contact form 
def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Your form has been submitted successfully!")
            return redirect('cl_index')
        else:
            return messages.error(request, "Please fill out all fields!")
    return messages.error(request, "Invalid request!")


def index(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = Client.objects.get(userId=user_id)
    return render(request, 'client/index.html', {'user': user})


def aboutus(request):
    return render(request, 'client/aboutus.html')

def industries(request):
    return render(request, 'client/industries.html')

def profile(request):
    return render(request, 'client/profile.html')

def test(request):
    return render(request, 'client/test.html')

def postajob(request):
    return render(request, 'client/postajob.html')
    
def logout(request):
    request.session.flush()  # ✅ Clears all session data (logs user out)
    return redirect('login')
    
