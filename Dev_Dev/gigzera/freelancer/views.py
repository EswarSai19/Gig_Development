from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact, ProjectsDisplay
from .forms import ContactForm


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

def test(request):
    return render(request, 'freelancer/test.html')

def jobs_test(request):
    jobs = ProjectsDisplay.objects.all()
    for job in jobs:
        job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    context = {'jobs': jobs}
    return render(request, 'freelancer/jobs_test.html', context)

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

