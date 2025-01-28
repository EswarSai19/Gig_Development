from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.jobs, name='jobs'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('industries/', views.industries, name='industries'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
  
]