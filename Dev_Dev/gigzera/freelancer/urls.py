from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='fl_index'),
    # path('index/', views.index, name='fl_index'),
    path('jobs/', views.jobs, name='fl_jobs'),
    path('aboutus/', views.aboutus, name='fl_aboutus'),
    path('industries/', views.industries, name='fl_industries'),
    path('profile/', views.profile, name='fl_profile'),
    path('test/', views.test, name='fl_test'),
    path('jobs_test/', views.jobs_test, name='fl_jobs_test'),
    # path('job_detail_partial', views.load_job_details, name='job_detail_partial'),
    path("load_job_details/", views.load_job_details, name="load_job_details"),
    path('projectTracking/', views.projectTracking, name='fl_projectTracking'),
    path('singleProjectTracking/', views.singleProjectTracking, name='fl_singleProjectTracking'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
  
]