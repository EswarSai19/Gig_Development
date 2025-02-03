from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact
from .forms import ContactForm
from freelancer.models import ProjectsDisplay, Freelancer, Skill
from client.models import Client

def index(request):
    jobs = ProjectsDisplay.objects.all().order_by('-created_at')[0:3]
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs}
    return render(request, 'non_register/index.html', context)

def jobs(request):
    jobs = ProjectsDisplay.objects.all().order_by('-created_at')
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs}
    print("Jobs: ", jobs)
    return render(request, 'non_register/jobs.html', context)

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
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Fetch user from both tables
        freelancer = Freelancer.objects.filter(email=email).first()
        client = Client.objects.filter(email=email).first()

        if freelancer and check_password(password, freelancer.password):
            request.session['user_id'] = freelancer.userId
            request.session['user_role'] = 'freelancer'
            return redirect('fl_index')  # Redirect to freelancer dashboard

        elif client and check_password(password, client.password):
            request.session['user_id'] = client.userId
            request.session['user_role'] = 'client'
            return redirect('cl_index')  # Redirect to client dashboard

        else:
            messages.error(request, 'Invalid credentials')

    return render(request, 'non_register/login.html')


def forgot(request):
    return render(request, 'non_register/forgot.html')

def test(request):
    jobs = ProjectsDisplay.objects.all()
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs}
    return render(request, 'non_register/test.html', context)

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

# Freelancer form
def submit_freelancer(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        education = request.POST.get("education")
        certifications = request.POST.get("certifications")
        experience = request.POST.get("experience")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        social_media = request.POST.get("social_media")
        
        # Collect skills and experiences
        skills = {}
        for i in range(1, 4):  # Adjust range if you have more skill fields
            skill = request.POST.get(f"skill{i}")
            exp = request.POST.get(f"experience{i}")
            if skill and exp:
                skills[skill] = float(exp)  # Convert experience to float
                
            
        # Save Freelancer object
        if password1 == password2:
            if Freelancer.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return render(request, "non_register/findajob.html")
            else:
                freelancer = Freelancer(
                    name=name,
                    phone=phone,
                    email=email,
                    education=education,
                    certifications=certifications,
                    experience=experience,
                    skills=skills,
                    social_media=social_media,
                    password=password1,
                )
                freelancer.save()
                for i in range(1,4):
                    skill = request.POST.get(f"skill{i}")
                    exp = request.POST.get(f"experience{i}")
                    if skill and exp:
                        Skill.objects.create(freelancer=freelancer, skill_name=skill, experience_years=exp)
                return render(request, "non_register/login.html")  # Redirect to success page
        else:
            messages.info(request, "Password does not match")
            return render(request, "non_register/findajob.html")

        
    return render(request, "non_register/findajob.html")

def submit_client(request):
    if request.method == "POST":
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        email = request.POST.get("email")
        selected_company = request.POST.get("selected_company")
        other_company = request.POST.get("other_company")
        designation = request.POST.get("designation")
        password1 = request.POST.get("password1")
        password2 = request.POST.get("password2")
        social_media = request.POST.get("social_media")

        # Assign the non-empty value
        company = other_company if other_company else selected_company

        # Save Freelancer object
        if password1 == password2:
            if Client.objects.filter(email=email).exists():
                messages.info(request, "Email already exists")
                return render(request, "non_register/postajob.html")
            else:
                client = Client(
                    name=name,
                    phone=phone,
                    email=email,
                    company=company,
                    designation=designation,
                    social_media=social_media,
                    password=password1,
                )
                client.save()
                return render(request, "non_register/login.html")
        else:
            messages.info(request, "Password does not match")
            return render(request, "non_register/postajob.html")
    return render(request, "non_register/postajob.html")