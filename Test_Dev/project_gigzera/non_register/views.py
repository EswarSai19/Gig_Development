from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

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