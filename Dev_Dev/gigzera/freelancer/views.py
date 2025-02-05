from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import ProjectsDisplay, Freelancer, Skill
from non_register.models import Contact
from django.core.files.storage import FileSystemStorage
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    jobs = ProjectsDisplay.objects.all().order_by('-created_at')
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs, 'user': user}    
    return render(request, 'freelancer/jobs.html', context)

def aboutus(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    context = {'user': user}
    return render(request, 'freelancer/aboutus.html', context)

def industries(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    context = {'user': user}
    return render(request, 'freelancer/industries.html', context)

def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    context = {'user': user}
    return render(request, 'freelancer/profile.html', context)

def test(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    context = {'user': user}
    return render(request, 'freelancer/test.html', context)



def edit_freelancer(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    freelancer = get_object_or_404(Freelancer, userId=user_id)

    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the data from the request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        social_media = request.POST.get('social_media')
        # experience = request.POST.get('experience')

        # Handle file upload for profilePic
        profile_pic = request.FILES.get('profilePic')
        if profile_pic:
            fs = FileSystemStorage(location='media/freelancer/profile_pics/')
            filename = fs.save(profile_pic.name, profile_pic)
            profile_pic_url = fs.url(filename)  # URL of the uploaded file
        else:
            profile_pic_url = freelancer.profilePic  # Keep the existing picture if no new one is uploaded

        # Update the freelancer instance
        freelancer.name = name
        freelancer.phone = phone
        freelancer.email = email
        freelancer.designation = designation
        freelancer.social_media = social_media
        freelancer.profilePic = profile_pic_url  # Update the profile picture URL

        # Save the updated freelancer object
        freelancer.save()

        # Redirect to a new page or display a success message
        return redirect('fl_test')

    return render(request, 'freelancer/fl_test.html', {'user': freelancer})



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
            return redirect("fl_jobs")

        # Validate Inputs
        if not opportunityId or not budget or not time_estimation or not comments:
            messages.error(request, "All fields are required.")
            return redirect("fl_jobs")

        # Fetch Freelancer Object
        try:
            freelancer = Freelancer.objects.get(userId=freelancer_id)
        except Freelancer.DoesNotExist:
            messages.error(request, "Freelancer not found.")
            return redirect("fl_jobs")

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
        return redirect("fl_jobs")

    return redirect("fl_jobs")


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
            user_type='freelancer',
            user_id=user_id,
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

