

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact
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
    # jobs = ProjectsDisplay.objects.all().order_by('-created_at')[0:3]
    # for job in jobs:
    #     job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    # context = {'jobs': jobs}
    return render(request, 'client/index.html')

# def jobs(request):
#     jobs = ProjectsDisplay.objects.all().order_by('-created_at')[0:3]
#     for job in jobs:
#         job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
#     context = {'jobs': jobs}
#     return render(request, 'client/jobs.html', context)

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

