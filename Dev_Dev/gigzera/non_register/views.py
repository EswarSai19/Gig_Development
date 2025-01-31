from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact, Freelancer, Skill, Certificate
from .forms import ContactForm, FreelancerForm, SkillFormSet, CertificateFormSet
from freelancer.models import ProjectsDisplay
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

        try:
            user = Freelancer.objects.get(email=email)  # Get user by email
            if check_password(password, user.password):  # Check encrypted password
                # return render(request, 'non_register/index.html')
                return redirect('fl_index')  # Redirect to 'index' page after login
            else:
                messages.error(request, 'Invalid credentials')
                return redirect('login')  # Use redirect instead of render for better UX
        except Freelancer.DoesNotExist:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

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


# def submit_freelancer(request):
#     if request.method == 'POST':
#         freelancer_form = FreelancerForm(request.POST, request.FILES)
        
#         if freelancer_form.is_valid():
#             freelancer = freelancer_form.save(commit=False)
#             freelancer.user = request.user  # Associate with the logged-in user, if needed
#             freelancer.save()

#             skill_formset = SkillFormSet(request.POST, instance=freelancer)
#             certificate_formset = CertificateFormSet(request.POST, instance=freelancer)

#             if skill_formset.is_valid() and certificate_formset.is_valid():
#                 skill_formset.save()
#                 certificate_formset.save()

#                 messages.success(request, "Freelancer details submitted successfully!")
#                 return redirect('login')  # Redirect to 'login' page after success
#             else:
#                 messages.error(request, "Please correct the errors in the skill or certificate forms.")
#         else:
#             # Initialize formsets even when the main form is invalid
#             skill_formset = SkillFormSet(request.POST)
#             certificate_formset = CertificateFormSet(request.POST)
#             messages.error(request, "Please correct the errors in the main Freelancer form.")
#     else:
#         freelancer_form = FreelancerForm()
#         skill_formset = SkillFormSet()
#         certificate_formset = CertificateFormSet()

#     return render(request, 'non_register/login.html', {
#         'freelancer_form': freelancer_form,
#         'skill_formset': skill_formset,
#         'certificate_formset': certificate_formset,
#     })

