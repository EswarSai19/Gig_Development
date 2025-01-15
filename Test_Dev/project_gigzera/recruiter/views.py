from django.shortcuts import render

# Create your views here.
def re_index(request):
    return render(request, 'RE_index.html')