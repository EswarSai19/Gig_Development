from django.shortcuts import render

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
