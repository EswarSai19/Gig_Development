from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
import os
from django.conf import settings
from non_register.models import Contact
from django.core.files.storage import FileSystemStorage
from .models import ProjectQuote, Freelancer, EmploymentHistory, Certificate, Skill, ProjectsDisplay, ProjectStatusDetails  # Create a model for storing quotes
from django.core.exceptions import ValidationError
from datetime import datetime
# from django.contrib.auth.decorators import login_required

# To get initial of the username
def get_initials(name):
    # Split the name into parts
    name_parts = name.strip().split()
    
    # Extract the first letter from each part and capitalize it
    initials = ''.join(part[0].upper() for part in name_parts)
    
    return initials


def index(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    print(user.name, "Name")
    jobs = ProjectsDisplay.objects.all().order_by('-created_at')[0:3]
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    user.initials = get_initials(user.name)
    print(user.initials)
    context = {'jobs': jobs, 'user': user}    
    return render(request, 'freelancer/index.html', context)

def jobs(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
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
    user.initials = get_initials(user.name)
    context = {'user': user}
    return render(request, 'freelancer/aboutus.html', context)

def industries(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context = {'user': user}
    return render(request, 'freelancer/industries.html', context)

def profile(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context = {'user': user}
    return render(request, 'freelancer/profile.html', context)

def test(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing

    user = Freelancer.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    employment_history = EmploymentHistory.objects.filter(freelancer_id=user_id).order_by('-start_date')
    certificates = Certificate.objects.filter(freelancer_id=user_id).order_by('-issue_date')
    skills = Skill.objects.filter(freelancer_id=user_id).order_by('-updated_at')

    context = {
        'user': user,
        'employment_history': employment_history,  # Corrected the assignment
        'certificates': certificates,
        'skills':skills
    }
    return render(request, 'freelancer/test.html', context)


# Profile summary editing
def edit_profile_summary(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')
    
    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)

    if request.method == 'POST':
        profile_summary = request.POST.get('profile_summary')
        print(f"Received Summary: {profile_summary}")  # Debugging
        
        if profile_summary:
            freelancer.profile_summary = profile_summary
            freelancer.save()
            print(f"Updated Summary: {freelancer.profile_summary}")
        else:
            print("No summary received in POST request.")

        return redirect('fl_test')

    return render(request, 'freelancer/test.html', {'user': freelancer})

# Work history related
def add_work_history(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)

    if request.method == 'POST':
        # Retrieve form data
        company = request.POST.get('company')
        job_title = request.POST.get('job_title')
        description = request.POST.get('description')
        city = request.POST.get('city')
        country = request.POST.get('country')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')

        # Checkbox handling
        currently_working = request.POST.get('currently_working') == 'on'

        print("Here are the details\n", company, job_title, description, city, country, start_date, end_date, currently_working)

        # Validation (end_date is optional if currently working)
        if not all([company, job_title, description, city, country, start_date]):
            messages.error(request, "Please fill out all required fields!")
            return redirect('fl_test')

        if not currently_working and not end_date:
            messages.error(request, "Please provide an end date if you're not currently working.")
            return redirect('fl_test')

        end_date = end_date if not currently_working else None  # Clear end date if currently working

        EmploymentHistory.objects.create(
            company = company,
            job_title = job_title,
            description = description,
            city = city,
            country = country,
            start_date = start_date,
            end_date = end_date,
            currently_working = currently_working,
            freelancer_id=user_id
        )

        # Redirect or show success message
        messages.success(request, "Work history updated successfully!")
        return redirect('fl_test')

    return render(request, 'freelancer/test.html', {'user': freelancer})

def edit_job(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)
    job_id = request.POST.get('job_id')
    job = get_object_or_404(EmploymentHistory, id=job_id)
    if request.method == 'POST':
        job_id = request.POST.get('job_id')
        company = request.POST.get('company')
        city = request.POST.get('city')
        country = request.POST.get('country')
        job_title = request.POST.get('job_title')
        description = request.POST.get('description')
        start_date = request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        currently_working = request.POST.get('currently_working') == 'on'

        # Handle end_date if currently_working is True
        if currently_working:
            end_date = None

        try:
            # Validate start_date
            start_date_obj = datetime.strptime(start_date, '%Y-%m-%d')

            # Validate end_date only if it's provided
            end_date_obj = None
            if end_date:
                end_date_obj = datetime.strptime(end_date, '%Y-%m-%d')

            # Update the job in the database (pseudo-code)
            job.company = company
            job.city = city
            job.country = country
            job.job_title = job_title
            job.description = description
            job.start_date = start_date_obj
            job.end_date = end_date_obj
            job.currently_working = currently_working
            job.save()
            messages.success(request, "Work history details edited successfully!")
            return redirect('fl_test')  # Redirect back to dashboard after saving
        except ValueError as e:
            message.error(request, ValidationError(f"Invalid date format: {e}"))
            return redirect('fl_test')

    return render('freelancer/fl_test.html', {'user':freelancer})  # Redirect to an error page if not POST

def delete_job(request, job_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)
    print("I am inside delete job", job_id)
    if request.method == 'POST':
        job = get_object_or_404(EmploymentHistory, id=job_id)
        job.delete()
        return redirect('fl_test')  # Replace with your dashboard or relevant page name
    return render(request, 'freelancer/fl_test.html', {'user': freelancer})


# certificates related
def add_certification(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)

    if request.method == 'POST':
        # Retrieve form data
        cert_name = request.POST.get('cert_name')
        issue_date = request.POST.get('issue_date')
        expiry_date = request.POST.get('end_date')
        cert_id = request.POST.get('cert_id')
        cert_url = request.POST.get('cert_url')


        print("Here are the details\n", cert_name, issue_date, expiry_date, cert_id, cert_url)

        # Validation (end_date is optional if currently working)
        if not all([cert_name, issue_date]):
            messages.error(request, "Please fill out all required fields!")
            return redirect('fl_test')

        Certificate.objects.create(
            certificate_name = cert_name,
            issue_date = issue_date,
            expiry_date = expiry_date,
            certification_id = cert_id,
            certification_url = cert_url,
            freelancer_id=user_id
        )

        current_certifications = freelancer.certifications
        certificates_list = current_certifications.split(',') if current_certifications else []

        # Append the new certificate name (strip extra spaces)
        certificates_list.append(cert_name.strip())

        # Update the freelancer's certifications with the new list
        freelancer.certifications = ','.join(certificates_list)
        freelancer.save()

        # Redirect or show success message
        messages.success(request, "Certification added successfully!")
        return redirect('fl_test')

    return render(request, 'freelancer/test.html', {'user': freelancer})

def edit_cert(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)
    cert_id = request.POST.get('cert_id')
    job = get_object_or_404(Certificate, id=cert_id)
    if request.method == 'POST':
        cert_id = request.POST.get('cert_id')
        cert_name = request.POST.get('cert_name')
        issue_date = request.POST.get('issue_date')
        expiry_date = request.POST.get('expiry_date')
        certification_id = request.POST.get('certification_id')
        cert_url = request.POST.get('cert_url')

        try:
            # Validate issue_date
            issue_date_obj = datetime.strptime(issue_date, '%Y-%m-%d')

            # Validate end_date only if it's provided
            expiry_date_obj = None
            if expiry_date:
                expiry_date_obj = datetime.strptime(expiry_date, '%Y-%m-%d')

            # Update the job in the database (pseudo-code)
            job.certificate_name = cert_name
            job.issue_date = issue_date
            job.expiry_date = expiry_date
            job.certification_id = certification_id
            job.certification_url = cert_url
            job.freelancer_id = user_id

            job.save()
            messages.success(request, "Certication details edited successfully!")
            return redirect('fl_test')  # Redirect back to dashboard after saving
        except ValueError as e:
            message.error(request, ValidationError(f"Invalid date format: {e}"))
            return redirect('fl_test')

    return render('freelancer/fl_test.html', {'user':freelancer}) 

def delete_cert(request, cert_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing

    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)
    print("I am inside delete job", cert_id)

    if request.method == 'POST':
        # Get the certificate to be deleted
        job = get_object_or_404(Certificate, id=cert_id)

        # Get the existing certificates (comma-separated) for the freelancer
        current_certificates = freelancer.certifications
        certificates_list = current_certificates.split(',') if current_certificates else []
        print(certificates_list, "List")
        print(job.certificate_name, "cert name")

        # Remove the deleted certificate from the list
        certificates_list = [cert.strip() for cert in certificates_list]
        if job.certificate_name.strip() in certificates_list:
            certificates_list.remove(job.certificate_name.strip())

        print(certificates_list, "After removing from list of cert table")

        # Update the certificates field in the freelancer record
        freelancer.certifications = ','.join(certificates_list)
        freelancer.save()

        # Delete the certificate
        job.delete()

        return redirect('fl_test')  # Replace with your dashboard or relevant page name

    return render(request, 'freelancer/fl_test.html', {'user': freelancer})


# Skills related

def delete_skill(request, skill_id):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing

    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)
    print("Inside delete skill", skill_id)

    if request.method == 'POST':
        # Get the skill to be deleted
        skill = get_object_or_404(Skill, id=skill_id, freelancer=freelancer)

        # Check if skills is a string or dict before loading
        if isinstance(freelancer.skills, str):
            current_skills = json.loads(freelancer.skills) if freelancer.skills else {}
        elif isinstance(freelancer.skills, dict):
            current_skills = freelancer.skills
        else:
            current_skills = {}

        print("Current skills:", current_skills)

        # Remove the skill from the JSON field
        skill_name = skill.skill_name
        if skill_name in current_skills:
            del current_skills[skill_name]
            print(f"Removed {skill_name} from freelancer's skills")

        # Convert dictionary back to JSON string and update the Freelancer's skills field
        freelancer.skills = current_skills
        freelancer.save()

        # Delete the skill from the Skill table
        skill.delete()

        return redirect('fl_test')  # Redirect to your dashboard or relevant page

    return render(request, 'freelancer/fl_test.html', {'user': freelancer})

def add_skill(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    freelancer = get_object_or_404(Freelancer, userId=user_id)
    freelancer.initials = get_initials(freelancer.name)

    if request.method == 'POST':
        # Retrieve form data
        new_skill = request.POST.get('new_skill')
        new_exp = request.POST.get('new_exp')


        print("Here are the details\n", new_skill, new_exp)

        # Validation (end_date is optional if currently working)
        if not all([new_skill, new_exp]):
            messages.error(request, "Please fill out all required fields!")
            return redirect('fl_test')

        Skill.objects.create(
            skill_name = new_skill,
            experience_years = new_exp,
            freelancer_id=user_id
        )

        # Check if skills is a string or dict before loading
        if isinstance(freelancer.skills, str):
            current_skills = json.loads(freelancer.skills) if freelancer.skills else {}
        elif isinstance(freelancer.skills, dict):
            current_skills = freelancer.skills
        else:
            current_skills = {}

        print("Current skills:", current_skills)
        current_skills[new_skill] = new_exp

        freelancer.skills = current_skills
        freelancer.save()

        # Redirect or show success message
        messages.success(request, "New skill added successfully!")
        return redirect('fl_test')

    return render(request, 'freelancer/test.html', {'user': freelancer})



# Freelancer changes
def edit_freelancer(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
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
            fs = FileSystemStorage(location=os.path.join(settings.MEDIA_ROOT, 'freelancer/profile_pics'))
            filename = fs.save(profile_pic.name, profile_pic)
            freelancer.profilePic = f'freelancer/profile_pics/{filename}'  # Save relative path instead of URL
            print("Profile pic uploaded:", freelancer.profilePic)
        else:
            print("Using existing profile pic:", freelancer.profilePic)
            freelancer.profilePic = f'freelancer/profile_pics/default_profile.png'

        # Update the freelancer instance
        freelancer.name = name
        freelancer.phone = phone
        freelancer.email = email
        freelancer.designation = designation
        freelancer.social_media = social_media

        # Save the updated freelancer object
        freelancer.save()

        # Redirect to a new page or display a success message
        return redirect('fl_test')

    return render(request, 'freelancer/fl_test.html', {'user': freelancer})


def delete_profile_pic(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    freelancer = get_object_or_404(Freelancer, userId=user_id)

    if freelancer.profilePic:
        # Construct the full path to the profile picture
        profile_pic_path = os.path.join(settings.MEDIA_ROOT, freelancer.profilePic.name)

        # Check if file exists and delete it
        if os.path.isfile(profile_pic_path):
            os.remove(profile_pic_path)
            print(f"Deleted file: {profile_pic_path}")
        else:
            print("File not found on disk:", profile_pic_path)

        # Clear the profilePic field in the database
        freelancer.profilePic = "freelancer/profile_pics/default_profile.png"
        freelancer.save()
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
    user.initials = get_initials(user.name)
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
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    print("Userid", user_id)
    # Step 1: Use filter() to get multiple project records
    projects = ProjectStatusDetails.objects.filter(freelancer_id=user_id)
    status_dict = {project.opportunity_id: project.status for project in projects}
    opportunity_ids = projects.values_list('opportunity_id', flat=True)

    print(opportunity_ids, "IDs")
    
    filtered_jobs = ProjectsDisplay.objects.filter(opportunityId__in=opportunity_ids)

    context = {
        'user': user,
        'projects': projects,
        'filtered_jobs': filtered_jobs,
        'status_dict': status_dict  # Use this in your template
    }
    print("Jobs", filtered_jobs)
    return render(request, 'freelancer/projectTracking.html', context)

def singleProjectTracking(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')  # Redirect to login if session is missing
    user = Freelancer.objects.get(userId=user_id)
    user.initials = get_initials(user.name)
    context = {'user': user}
    return render(request, 'freelancer/singleProjectTracking.html', context)

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

