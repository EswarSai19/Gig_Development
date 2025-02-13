from django.shortcuts import render, redirect

# Create your views here.
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
    return render(request, 'myadmin/latestProjectQuotes.html')

def jobPageAdv(request):
    return render(request, 'myadmin/jobPageAdv.html')

def jobPageImages(request):
    return render(request, 'myadmin/jobPageImages.html')

def partnerLogos(request):
    return render(request, 'myadmin/partnerLogos.html')

def logout(request):
    return render(request, 'myadmin/ad_logout.html')
