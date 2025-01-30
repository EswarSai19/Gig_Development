from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='fl_index'),
    # path('index/', views.index, name='fl_index'),
    path('jobs/', views.jobs, name='fl_jobs'),
    path('aboutus/', views.aboutus, name='fl_aboutus'),
    path('industries/', views.industries, name='fl_industries'),
    path('profile/', views.profile, name='fl_profile'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
  
]