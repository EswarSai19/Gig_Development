from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
# from .models import Freelancer, Skill
from .models import Contact
from django.http import HttpResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from .models import Freelancer, Skill
import json

# Contact form 
def submit_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone_number = request.POST.get('phone_number')
        reason = request.POST.get('reason')
        description = request.POST.get('description')

        if name and phone_number and reason and description:
            # Save the form data to the database
            Contact.objects.create(
                name=name,
                phone_number=phone_number,
                reason=reason,
                description=description
            )
            messages.success(request, "Your form has been submitted successfully!")
            return redirect('home')  # Change to redirect or render a success page
        else:
            return HttpResponse("Please fill out all fields!", status=400)

    return HttpResponse("Invalid request!", status=400)

# Create your views here.
def home(request):
    return render(request, 'home.html')

def test(request):
    return render(request, 'test.html')

def jobs(request):
    return render(request, 'jobs.html')

def aboutus(request):
    return render(request, 'aboutus.html')

def industries(request):
    return render(request, 'industries.html')

def login(request):
    return render(request, 'login.html')

def signup(request):
    return render(request, 'signup.html')

def forget(request):
    return render(request, 'forget.html')

def postajob(request):
    return render(request, 'postajob.html')

# def findajob(request):
#     return render(request, 'findajob.html')



def findajob(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('name')
        profile_pic = request.FILES.get('profilePic')  # For file upload
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        user_role = request.POST.get('user_role')
        country = request.POST.get('country')
        social_media = request.POST.get('social_media')
        education = request.POST.get('education')
        certifications = request.POST.getlist('certifications')  # Multiple values
        experience = request.POST.get('experience')
        skills = request.POST.get('skills')  # JSON string for skills
        password = request.POST.get('password')
        projects_assigned = request.POST.getlist('projects_assigned')
        project_status = request.POST.getlist('project_status')

        # Validation for required fields
        if not all([name, phone, email, education, experience, social_media, skills, certifications, password]):
            messages.error(request, "Please fill out all required fields!")
            return redirect('findajob')  # Replace with your registration page URL name

        # Create Freelancer object
        try:
            freelancer = Freelancer.objects.create(
                name=name,
                profilePic=profile_pic,
                phone=phone,
                email=email,
                user_role=user_role,
                country=country,
                social_media=social_media,
                education=education,
                certifications=certifications,
                experience=experience,
                skills=json.loads(skills) if skills else {},  # Parse JSON string to Python dict
                password=password,  # Ideally, hash the password
                projects_assigned=projects_assigned,
                project_status=project_status,
            )

            # Add associated skills (if provided)
            if skills:
                parsed_skills = json.loads(skills)  # Assuming skills is sent as a JSON string
                for skill_name, exp_years in parsed_skills.items():
                    Skill.objects.create(
                        freelancer=freelancer,
                        skill_name=skill_name,
                        experience_years=int(exp_years),
                    )

            messages.success(request, "Freelancer registered successfully!")
            return redirect('login')  # Replace 'home' with the page you want to redirect to after registration

        except Exception as e:
            messages.error(request, f"An error occurred: {str(e)}")
            return redirect('findajob')

    return render(request, 'findajob.html')  # Render the registration form template


# def findajob(request):
#     if request.method == 'POST':
#         print("Post information",request.POST)
#         full_name = request.POST.get('fullName', '')  # Use .get() to avoid KeyError
#         phone = request.POST.get('phone', 0)
#         email = request.POST.get('email', '')
#         education = request.POST.get('education', '')
#         certifications = request.POST.get('certifications', '')
#         total_experience = int(request.POST.get('experience', 0))
#         linkedin = request.POST.get('linkedin', '')
#         password = make_password(request.POST.get('Password', ''))  # Hash the password

#         # Save freelancer details
#         freelancer = Freelancer.objects.create(
#             name=full_name,
#             phone=phone,
#             email=email,
#             education=education,
#             certifications=certifications.split(',') if certifications else [],
#             experience=total_experience,
#             social_media=linkedin,
#             password=password,
#         )

#         # Save skills and their associated experience
#         skills = request.POST.getlist('skill')
#         experiences = request.POST.getlist('experience')

#         for skill, exp in zip(skills, experiences):
#             Skill.objects.create(
#                 freelancer=freelancer,
#                 skill_name=skill,
#                 experience_years=int(exp.split()[0]),  # Extract years as integer
#             )

#         return redirect('non_register:login')
#     return render(request, 'findajob.html')


# def findajob(request):
    if request.method == 'POST':
        full_name = request.POST['fullName']
        phone = request.POST['phone']
        email = request.POST['email']
        education = request.POST['education']
        certifications = request.POST['certifications']
        total_experience = int(request.POST['experience'])
        linkedin = request.POST['linkedin']
        password = make_password(request.POST['Password'])  # Hash the password

        # Save freelancer details
        freelancer = Freelancer.objects.create(
            full_name=full_name,
            phone=phone,
            email=email,
            education=education,
            certifications=certifications,
            total_experience=total_experience,
            linkedin=linkedin,
            password=password,
        )

        # Save skills and their associated experience
        skills = request.POST.getlist('skill')
        experiences = request.POST.getlist('experience')

        for skill, exp in zip(skills, experiences):
            Skill.objects.create(
                freelancer=freelancer,
                skill_name=skill,
                experience_years=int(exp.split()[0]),  # Extract years as integer
            )

        return redirect('non_register:login')
    return render(request, 'findajob.html')