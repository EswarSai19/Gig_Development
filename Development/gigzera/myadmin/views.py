from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User, auth
from django.contrib.auth.hashers import check_password, make_password
from django.http import HttpResponse
from django.contrib import messages
import json
import os
import locale
from django.conf import settings
from django.core.files.storage import FileSystemStorage
from db_schemas.models import Contact, ProjectQuote, Freelancer, EmploymentHistory, Certificate, Skill, ProjectsDisplay, ProjectStatusDetails  # Create a model for storing quotes
from django.core.exceptions import ValidationError
from datetime import datetime

# Create your views here.

def get_initials(name):
    # Split the name into parts
    name_parts = name.strip().split()
    # Extract the first letter from each part and capitalize it
    initials = ''.join(part[0].upper() for part in name_parts)
    return initials


currency_symbols = {
    "USD": "$", "EUR": "€", "JPY": "¥", "GBP": "£", "CNY": "¥", 
    "AUD": "A$", "CAD": "C$", "CHF": "CHF", "INR": "₹", "NZD": "NZ$"
}

def get_currency_symbol(currency_code):
    return currency_symbols.get(currency_code, "-")


# Currency formatting rules
currency_symbols = {
    "USD": "$", "EUR": "€", "JPY": "¥", "GBP": "£", "CNY": "¥", 
    "AUD": "A$", "CAD": "C$", "CHF": "CHF", "INR": "₹", "NZD": "NZ$"
}

# Locale settings for number formatting
currency_locales = {
    "USD": "en_US", "EUR": "de_DE", "JPY": "ja_JP", "GBP": "en_GB", "CNY": "zh_CN", 
    "AUD": "en_AU", "CAD": "en_CA", "CHF": "de_CH", "INR": "en_IN", "NZD": "en_NZ"
}

def format_currency(amount, currency_code):
    """Formats the number according to the given currency locale."""
    try:
        amount = int(str(amount).replace(",", ""))  # Remove commas and convert to integer
        locale.setlocale(locale.LC_ALL, currency_locales.get(currency_code, "en_US"))  # Set locale
        formatted_amount = locale.format_string("%d", amount, grouping=True)  # Format with commas
        return f"{currency_symbols.get(currency_code, '')} {formatted_amount}"  # Add currency symbol
        # return f"{formatted_amount}"  # Add currency symbol
    except ValueError:
        return "Invalid amount"

def add_and_format(budget, admin_margin, currency_code):
    """Adds two numbers and formats them based on the currency code."""
    budget = int(str(budget).replace(",", ""))  # Convert budget to integer
    admin_margin = int(str(admin_margin).replace(",", ""))  # Convert admin margin to integer
    total = budget + admin_margin  # Calculate sum
    return format_currency(total, currency_code)  # Format according to currency

# Example usage
# print(add_and_format("2,00,000", "5,000", "INR"))  # Output: ₹ 2,05,000
# print(add_and_format("200000", "5000", "USD"))  # Output: $ 205,000
# print(add_and_format("1,220,000", "5,000", "USD"))  # Output: $ 1,225,000

def ad_index(request):
    return render(request, 'myadmin/ad_index.html')

def dashboard(request):
    return render(request, 'myadmin/dashboard.html')

def freelancers(request):
    return render(request, 'myadmin/freelancers.html')

def clients(request):
    return render(request, 'myadmin/clients.html')
    
def ongoingProjects(request):
    return render(request, 'myadmin/ongoingProjects.html')

def yourProjects(request):
    return render(request, 'myadmin/yourProjects.html')

def userManagement(request):
    return render(request, 'myadmin/userManagement.html')

def latestProjectQuotes(request):
    bids = ProjectQuote.objects.all().order_by('-created_at')
    for bid in bids:
        job = ProjectsDisplay.objects.filter(opportunityId=bid.opportunityId).first()
        user = Freelancer.objects.filter(userId=bid.freelancer_id).first()
        bid.title = job.title if job else "No Title"  # Fixed variable name
        bid.cur_symbol = get_currency_symbol(job.currency if job else "USD")  # Ensure currency is handled properly
        bid.user_experience = user.experience if user else "No Experience"
    
    context = {'bids': bids}
    return render(request, 'myadmin/latestProjectQuotes.html', context)

def latestSinglePQ(request):
    opportunity_id = request.GET.get('opportunityId')
    user_id = request.GET.get('userId')
    bid_id = request.GET.get('bidId')
    print("ID", opportunity_id, user_id, bid_id)

    job = ProjectsDisplay.objects.filter(opportunityId=opportunity_id).first()
    job.deliverables_list = [line.strip() for line in job.deliverables.split("\n")]
    job.skills_list = [skill.strip().title() for skill in job.skills_required.split(',')]
    job.cur_symbol = get_currency_symbol(job.currency)


    user = Freelancer.objects.filter(userId=user_id).first()
    user.skills_dict = {skill: f"{exp} years" for skill, exp in user.skills.items()}
    user.certificates_list = [cert.strip().title() for cert in user.certifications.split(',')]

    bid = ProjectQuote.objects.filter(projectQuoteId=bid_id).first()
    bid.cur_symbol = get_currency_symbol(job.currency if job else "USD")
    print("Job", bid)
    context = {'job':job, 'user':user, 'bid':bid}
    return render(request, 'myadmin/latestSinglePQ.html', context)

def bidApproved(request):
    bids = ProjectQuote.objects.all().order_by('-created_at')
    for bid in bids:
        job = ProjectsDisplay.objects.filter(opportunityId=bid.opportunityId).first()
        user = Freelancer.objects.filter(userId=bid.freelancer_id).first()
        bid.title = job.title if job else "No Title"  # Fixed variable name
        bid.cur_symbol = get_currency_symbol(job.currency if job else "USD")  # Ensure currency is handled properly
        bid.user_experience = user.experience if user else "No Experience"
        context = {'bids': bids}
    if request.method == "POST":
        admin_margin = request.POST.get("adminMargin", "0").strip()
        bid_id = request.POST.get('bidId')
        print("Admin Margin:", admin_margin, bid_id)  # Debugging
        try:
            # Fetch the bid using bid_id
            bid = get_object_or_404(ProjectQuote, projectQuoteId=bid_id)  
            
            # Update the admin margin and bid status
            bid.admin_margin = admin_margin
            bid.admin_bid_status = "approved"
            bid.revised_budget = add_and_format(bid.budget, bid.admin_margin, bid.currency)
            bid.save()  # Save changes

            print(f"Updated bid {bid_id}: admin_margin={admin_margin}, bid_status=approved")
            messages.success(request, "Bid was sent to client successfully")
            return redirect('ad_latestProjectQuotes')

        except Exception as e:
            print(f"Error updating bid: {e}")
            messages.error(request, f"Error updating bid {bid_id}: {str(e)}")
    return render(request, 'myadmin/latestProjectQuotes.html', context)

def bidRejected(request):
    bids = ProjectQuote.objects.all().order_by('-created_at')
    for bid in bids:
        job = ProjectsDisplay.objects.filter(opportunityId=bid.opportunityId).first()
        user = Freelancer.objects.filter(userId=bid.freelancer_id).first()
        bid.title = job.title if job else "No Title"  # Fixed variable name
        bid.cur_symbol = get_currency_symbol(job.currency if job else "USD")  # Ensure currency is handled properly
        bid.user_experience = user.experience if user else "No Experience"
        context = {'bids': bids}
    if request.method == "POST":
        admin_margin = request.POST.get("adminMargin", "0").strip()
        bid_id = request.POST.get('bidId')
        print("Admin Margin:", admin_margin, bid_id)  # Debugging
        try:
            # Fetch the bid using bid_id
            bid = get_object_or_404(ProjectQuote, projectQuoteId=bid_id)  
            
            # Update the admin margin and bid status
            bid.admin_margin = admin_margin
            bid.admin_bid_status = "rejected"
            bid.revised_budget = add_and_format(bid.budget, bid.admin_margin, job.currency)
            bid.save()  # Save changes

            print(f"Updated bid {bid_id}: admin_margin={admin_margin}, bid_status=approved")
            messages.success(request, "Bid was rejected successfully")
            return redirect('ad_latestProjectQuotes')

        except Exception as e:
            print(f"Error updating bid: {e}")
            messages.error(request, f"Error updating bid {bid_id}: {str(e)}")
    return render(request, 'myadmin/latestProjectQuotes.html', context)

def profileView(request):
    user_id = request.GET.get('userId')
    bid_id = request.GET.get('bidId')
    opportunity_id = request.GET.get('opportunityId')
    print("Coming",user_id, bid_id, opportunity_id)
    user = Freelancer.objects.filter(userId=user_id).first()
    user.initials = get_initials(user.name)
    employment_history = EmploymentHistory.objects.filter(freelancer_id=user_id).order_by('-start_date')
    certificates = Certificate.objects.filter(freelancer_id=user_id).order_by('-issue_date')
    skills = Skill.objects.filter(freelancer_id=user_id).order_by('-updated_at')

    context = {
        'user': user,
        'employment_history': employment_history,  # Corrected the assignment
        'certificates': certificates,
        'skills':skills,
        'bid_id':bid_id,
        'opportunity_id':opportunity_id,
        'user_id':user_id,
    }
    print("User id is", user_id )
    print("skills", skills )
    print("certificates", certificates )
    return render(request, 'myadmin/profileView.html', context)

def jobPageAdv(request):
    return render(request, 'myadmin/jobPageAdv.html')

def jobPageImages(request):
    return render(request, 'myadmin/jobPageImages.html')

def partnerLogos(request):
    return render(request, 'myadmin/partnerLogos.html')

def logout(request):
    return render(request, 'myadmin/ad_logout.html')
