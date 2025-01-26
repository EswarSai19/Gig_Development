from django.shortcuts import render, redirect
# from django.contrib.auth.hashers import make_password
from django.http import HttpResponse
from django.contrib import messages
import json
from .models import Contact
from .forms import ContactForm, FreelancerForm, SkillFormSet, CertificateFormSet

def index(request):
    return render(request, 'non_register/index.html')

def jobs(request):
    return render(request, 'non_register/jobs.html')

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
    return render(request, 'non_register/login.html')

def forgot(request):
    return render(request, 'non_register/forgot.html')

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


def submit_freelancer(request):
    if request.method == 'POST':
        freelancer_form = FreelancerForm(request.POST, request.FILES)
        
        if freelancer_form.is_valid():
            freelancer = freelancer_form.save(commit=False)
            freelancer.user = request.user  # Associate with the logged-in user, if needed
            freelancer.save()

            skill_formset = SkillFormSet(request.POST, instance=freelancer)
            certificate_formset = CertificateFormSet(request.POST, instance=freelancer)

            if skill_formset.is_valid() and certificate_formset.is_valid():
                skill_formset.save()
                certificate_formset.save()

                messages.success(request, "Freelancer details submitted successfully!")
                return redirect('login')  # Redirect to 'login' page after success
            else:
                messages.error(request, "Please correct the errors in the skill or certificate forms.")
        else:
            messages.error(request, "Please correct the errors in the main Freelancer form.")
    else:
        freelancer_form = FreelancerForm()
        skill_formset = SkillFormSet()
        certificate_formset = CertificateFormSet()

    return render(request, 'submit_freelancer.html', {
        'freelancer_form': freelancer_form,
        'skill_formset': skill_formset,
        'certificate_formset': certificate_formset,
    })

