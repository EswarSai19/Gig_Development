from django.urls import path
from . import views

app_name= 'recruiter'

urlpatterns = [
    path('', views.re_index, name='RE_index')
]