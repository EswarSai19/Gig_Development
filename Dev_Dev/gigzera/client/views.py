

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
import os
from django.core.files.storage import FileSystemStorage
from django.conf import settings
from db_schemas.models import Client, ProjectsDisplay, Contact
from django.core.exceptions import ValidationError
from datetime import datetime

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

def get_initials(name):
    # Split the name into parts
    name_parts = name.strip().split()
    
    # Extract the first letter from each part and capitalize it
    initials = ''.join(part[0].upper() for part in name_parts)
    
    return initials


def cl_index(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    return render(request, 'client/index.html', {'user': user})


def cl_aboutus(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context={'user':user}
    return render(request, 'client/aboutus.html', context)

def cl_industries(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context={'user':user}
    return render(request, 'client/industries.html', context)

def cl_profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    print("users details:", user, user_id, user.initials)
    context={'user':user}

    if request.method=="POST":
        title=request.POST.get('title')
        project_type=request.POST.get('project_type')
        budget=request.POST.get('budget')
        duration=request.POST.get('duration')
        currency=request.POST.get('currency')
        description=request.POST.get('description')
        start_date=request.POST.get('start_date')
        requirements=request.POST.get('requirements')
        challenges=request.POST.get('challenges')
        time_zone=request.POST.get('time_zone')
        skills = request.POST.get("skills_list", "")  # Comma-separated string
        print(f"Selected Skills: {skills}") 

        if not all([title, project_type, budget, duration, currency, description, start_date, requirements, challenges, time_zone, skills]):
            messages.error(request, "Please fill out all fields!")
            return redirect('cl_postajob')  # Redirect to home page

        # Create and save the contact object
        ProjectsDisplay.objects.create(
            title=title, 
            project_type=project_type,
            budget= budget, 
            duration=duration, 
            currency=currency, 
            description=description, 
            start_date=start_date, 
            requirements=requirements, 
            challenges=challenges, 
            time_zone=time_zone, 
            skills_required=skills,
            client_id=user_id,
        )

        messages.success(request, "Your job has been submitted successfully!")
        return redirect('cl_profile')  # Redirect to home page

        print(f"title: {title}\nproject_type: {project_type}\nbudget: {budget}\nduration: {duration}\ncurrency: {currency}\ndescription: {description}\nstart_date: {start_date}\nrequirements: {requirements}\ntime_zone: {time_zone}\nchallenges: {challenges}\n")
    print("I am here")
    return render(request, 'client/cl_profile.html', context)

def cl_test(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context={'user':user}
    return render(request, 'client/test.html', context)

def cl_postajob(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context={'user':user}

    if request.method=="POST":
        title=request.POST.get('title')
        project_type=request.POST.get('project_type')
        budget=request.POST.get('budget')
        duration=request.POST.get('duration')
        currency=request.POST.get('currency')
        deliverables=request.POST.get('deliverables')
        description=request.POST.get('description')
        start_date=request.POST.get('start_date')
        requirements=request.POST.get('requirements')
        challenges=request.POST.get('challenges')
        time_zone=request.POST.get('time_zone')
        skills = request.POST.get("skills_list", "")  # Comma-separated string
        print(f"Selected Skills: {skills}") 

        if not all([title, project_type, budget, duration, currency, description, start_date, requirements, challenges, time_zone, skills]):
            messages.error(request, "Please fill out all fields!")
            return redirect('cl_postajob')  # Redirect to home page
        print("this is the testing user_id", user_id)
        # Create and save the contact object
        ProjectsDisplay.objects.create(
            title=title, 
            project_type=project_type,
            budget= budget, 
            duration=duration, 
            currency=currency, 
            description=description, 
            start_date=start_date,
            deliverables=deliverables,
            requirements=requirements, 
            challenges=challenges, 
            time_zone=time_zone, 
            skills_required=skills,
            client_id=user_id
        )

        messages.success(request, "Your form has been submitted successfully!")
        return redirect('cl_postajob')  # Redirect to home page

        print(f"title: {title}\nproject_type: {project_type}\nbudget: {budget}\nduration: {duration}\ncurrency: {currency}\ndescription: {description}\nstart_date: {start_date}\nrequirements: {requirements}\ntime_zone: {time_zone}\nchallenges: {challenges}\n")

    return render(request, 'client/cl_postajob.html', context)
    
def cl_logout(request):
    request.session.flush()  # ✅ Clears all session data (logs user out)
    return redirect('login')
    
def edit_profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    client = get_object_or_404(Client, userId=user_id)

    # Check if the request method is POST
    if request.method == 'POST':
        # Retrieve the data from the request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        designation = request.POST.get('designation')
        company = request.POST.get('company')
        social_media = request.POST.get('social_media')

        # Handle file upload for profilePic
        profile_pic = request.FILES.get('profilePic')
        if profile_pic:
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'client/profile_pics'))
            filename = fs.save(profile_pic.name, profile_pic)
            client.profilePic = f'client/profile_pics/{filename}'  # Save relative path instead of URL
            print("Profile pic uploaded:", client.profilePic)
        else:
            print("Using existing profile pic:", client.profilePic)
            client.profilePic = f'client/profile_pics/default_profile.png'
        print(name, email, phone, designation, social_media, company, profile_pic)
        # Update the client instance
        client.name = name
        client.phone = phone
        client.email = email
        client.designation = designation
        client.social_media = social_media
        client.company = company

        # Save the updated client object
        client.save()

        # Redirect to a new page or display a success message
        return redirect('cl_profile')

    return render(request, 'client/cl_profile.html', {'user': client})

def cl_ongoingProjects(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context={'user':user}
    return render(request, 'client/cl_ongoingProjects.html', context)

def cl_singleOgProject(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context={'user':user}
    return render(request, 'client/cl_singleOgProject.html', context)

def cl_viewBids(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context={'user':user}
    return render(request, 'client/cl_viewBids.html', context)

def cl_singleViewBid(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    user = Client.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context={'user':user}
    return render(request, 'client/cl_singleViewBid.html', context)





