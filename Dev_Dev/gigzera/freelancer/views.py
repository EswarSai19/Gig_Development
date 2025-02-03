from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact, ProjectsDisplay, Freelancer, Skill
from .forms import ContactForm


def index(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    jobs = ProjectsDisplay.objects.all().order_by('-created_at')[0:3]
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs, 'user': user}    
    return render(request, 'freelancer/index.html', context)

def jobs(request):
    jobs = ProjectsDisplay.objects.all().order_by('-created_at')[0:3]
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

def test(request):
    return render(request, 'freelancer/test.html')

def jobs_test(request):
    jobs = ProjectsDisplay.objects.all().order_by('-created_at')
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs}
    return render(request, 'freelancer/jobs_test.html', context)

def logout(request):
    request.session.flush()  # ✅ Clears all session data (logs user out)
    return redirect('login')


def load_job_details(request):
    job_id = request.POST.get("job_id")  # Get job ID from HTMX request
    job = get_object_or_404(ProjectsDisplay, opportunityId=job_id)
    # Process skills into a list for the selected job
    job.deliverables_list = [line.strip() for line in job.deliverables.split("\n")]
    job.requirements_list = [line.strip() for line in job.requirements.split("\n")]
    job.challenges_list = [line.strip() for line in job.challenges.split("\n")]
    job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    return render(request, "freelancer/job_detail_partial.html", {"job": job})

def projectTracking(request):
    return render(request, 'freelancer/projectTracking.html')

def singleProjectTracking(request):
    return render(request, 'freelancer/singleProjectTracking.html')

# Contact form 
def submit_contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, "Your form has been submitted successfully!")
            return redirect('fl_index')
        else:
            return messages.error(request, "Please fill out all fields!")
    return messages.error(request, "Invalid request!")

# Submit Form
# def submit_freelancer(request):
#     if request.method == "POST":
#         name = request.POST.get("name")
#         phone = request.POST.get("phone")
#         email = request.POST.get("email")
#         education = request.POST.get("education")
#         certifications = request.POST.get("certifications")
#         experience = request.POST.get("experience")
#         password1 = request.POST.get("password1")
#         password2 = request.POST.get("password2")
#         social_media = request.POST.get("social_media")
        
#         # Collect skills and experiences
#         skills = {}
#         for i in range(1, 4):  # Adjust range if you have more skill fields
#             skill = request.POST.get(f"skill{i}")
#             exp = request.POST.get(f"experience{i}")
#             if skill and exp:
#                 skills[skill] = float(exp)  # Convert experience to float
                
            
#         # Save Freelancer object
#         if password1 == password2:
#             if Freelancer.objects.filter(email=email).exists():
#                 messages.info(request, "Email already exists")
#                 return render(request, "non_register/findajob.html")
#             else:
#                 freelancer = Freelancer(
#                     name=name,
#                     phone=phone,
#                     email=email,
#                     education=education,
#                     certifications=certifications,
#                     experience=experience,
#                     skills=skills,
#                     social_media=social_media,
#                     password=password1,
#                 )
#                 freelancer.save()
#                 for i in range(1,4):
#                     skill = request.POST.get(f"skill{i}")
#                     exp = request.POST.get(f"experience{i}")
#                     if skill and exp:
#                         Skill.objects.create(freelancer=freelancer, skill_name=skill, experience_years=exp)
#                 return render(request, "non_register/login.html")  # Redirect to success page
#         else:
#             messages.info(request, "Password does not match")
#             return render(request, "non_register/findajob.html")

        
#     return render(request, "non_register/findajob.html")

