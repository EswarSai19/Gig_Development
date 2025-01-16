from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
# from .models import Freelancer, Skill

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

def findajob(request):
    
    return render(request, 'findajob.html')


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