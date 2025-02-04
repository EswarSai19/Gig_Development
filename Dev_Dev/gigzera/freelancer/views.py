from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import ProjectsDisplay, Freelancer, Skill
from non_register.models import Contact
from .models import ProjectQuote  # Create a model for storing quotes
# from django.contrib.auth.decorators import login_required

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


# @login_required
def submit_quote(request):
    if request.method == "POST":
        print(request.POST)
        opportunityId = request.POST.get("opportunity_id")
        budget = request.POST.get("budget")
        comments = request.POST.get("comments")
        time_estimation = request.POST.get("time_estimation")
        freelancer_id = request.session.get('user_id')  # Ensure it's stored in session

        if not freelancer_id:
            messages.error(request, "Freelancer session expired. Please log in again.")
            return redirect("login")
        if not opportunityId:
            messages.error(request, "opportunityId session expired.")
            return redirect("fl_jobs_test")

        # Validate Inputs
        if not opportunityId or not budget or not time_estimation or not comments:
            messages.error(request, "All fields are required.")
            return redirect("fl_jobs_test")

        # Fetch Freelancer Object
        try:
            freelancer = Freelancer.objects.get(userId=freelancer_id)
        except Freelancer.DoesNotExist:
            messages.error(request, "Freelancer not found.")
            return redirect("fl_jobs_test")

        # Debugging prints
        print(f"User ID from session: {freelancer_id}")
        print(f"Saving quote for {opportunityId} by {freelancer}")

        # Store in DB
        ProjectQuote.objects.create(
            freelancer=freelancer,  # Use ForeignKey if applicable
            opportunityId=opportunityId,
            budget=budget,
            time_estimation=time_estimation,
            comments=comments
        )

        messages.success(request, "Quote submitted successfully!")
        return redirect("fl_jobs_test")

    return redirect("fl_jobs_test")


def jobs_test(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    jobs = ProjectsDisplay.objects.all().order_by('-created_at')
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs, 'user': user}    
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
def fl_contact(request):
    if request.method == 'POST':
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
            user_type='freelancer',
            name=name,
            phone_number=phone_number,
            email=email,
            reason=reason,
            description=description
        )

        messages.success(request, "Your form has been submitted successfully!")
        return redirect('fl_index')  # Redirect to home page

    messages.error(request, "Invalid request!")
    return redirect(request.META.get('HTTP_REFERER', 'contact'))

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

