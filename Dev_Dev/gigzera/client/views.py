

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Client
from non_register.models import Contact

# Create your views here.
# Contact form 
def cl_contact(request):
    if request.method == 'POST':
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('login')  # Redirect to login if session is missing
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        email = request.POST.get('email')
        reason = request.POST.get('reason')
        description = request.POST.get('description')

        # Check if all fields are filled
        if not all([name, phone_number, email, reason, description]):
            messages.error(request, "Please fill out all fields!")
            return redirect(request.META.get('HTTP_REFERER', 'contact'))  # Redirect to the same page

        # Create and save the contact object
        Contact.objects.create(
            user_type='client',
            user_id=user_id,
            name=name,
            phone_number=phone_number,
            email=email,
            reason=reason,
            description=description
        )

        messages.success(request, "Your form has been submitted successfully!")
        return redirect('cl_index')  # Redirect to home page

    messages.error(request, "Invalid request!")
    return redirect(request.META.get('HTTP_REFERER', 'contact'))


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
    
