from django.shortcuts import render


# Create your views here.
def freelancer_index(request):
    return render(request, 'FL_index.html')