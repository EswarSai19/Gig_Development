from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='cl_index'),
    # path('index/', views.index, name='cl_index'),
    path('postajob/', views.postajob, name='cl_postajob'),
    path('aboutus/', views.aboutus, name='cl_aboutus'),
    path('industries/', views.industries, name='cl_industries'),
    path('profile/', views.profile, name='cl_profile'),
    path('test/', views.test, name='cl_test'),
    # path('jobs_test/', views.jobs_test, name='cl_jobs_test'),
    # path('job_detail_partial', views.load_job_details, name='job_detail_partial'),
    # path("load_job_details/", views.load_job_details, name="load_job_details"),
    # path('projectTracking/', views.projectTracking, name='cl_projectTracking'),
    # path('singleProjectTracking/', views.singleProjectTracking, name='cl_singleProjectTracking'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
  
]