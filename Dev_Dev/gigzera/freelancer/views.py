from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact
# from .forms import ContactForm, FreelancerForm, SkillFormSet, CertificateFormSet

def index(request):
    return render(request, 'freelancer/index.html')

def jobs(request):
    jobs = ProjectsDisplay.objects.all()
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs}
    return render(request, 'freelancer/jobs.html', context)

def aboutus(request):
    return render(request, 'freelancer/aboutus.html')

def industries(request):
    return render(request, 'freelancer/industries.html')

def profile(request):
    return render(request, 'freelancer/profile.html')
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

