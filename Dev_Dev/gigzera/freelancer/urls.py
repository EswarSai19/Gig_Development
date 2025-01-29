from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='freelancer_index'),
    # path('index/', views.index, name='freelancer_index'),
    path('jobs/', views.jobs, name='freelancer_jobs'),
    path('aboutus/', views.aboutus, name='freelancer_aboutus'),
    path('industries/', views.industries, name='freelancer_industries'),
    path('profile/', views.profile, name='freelancer_profile'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
  
]