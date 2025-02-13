from django.shortcuts import render, redirect
from db_schemas.models import ProjectQuote, ProjectsDisplay, Freelancer

# Create your views here.

currency_symbols = {
    "USD": "$", "EUR": "€", "JPY": "¥", "GBP": "£", "CNY": "¥", 
    "AUD": "A$", "CAD": "C$", "CHF": "CHF", "INR": "₹", "NZD": "NZ$"
}

def get_currency_symbol(currency_code):
    return currency_symbols.get(currency_code, "-")

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
    return render(request, 'myadmin/latestSinglePQ.html')

def profileView(request):
    return render(request, 'myadmin/profileView.html')

def jobPageAdv(request):
    return render(request, 'myadmin/jobPageAdv.html')

def jobPageImages(request):
    return render(request, 'myadmin/jobPageImages.html')

def partnerLogos(request):
    return render(request, 'myadmin/partnerLogos.html')

def logout(request):
    return render(request, 'myadmin/ad_logout.html')
