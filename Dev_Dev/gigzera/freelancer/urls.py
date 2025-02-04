from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='fl_index'),
    path('jobs/', views.jobs, name='fl_jobs'),
    path('aboutus/', views.aboutus, name='fl_aboutus'),
    path('industries/', views.industries, name='fl_industries'),
    path('profile/', views.profile, name='fl_profile'),
    path('test/', views.test, name='fl_test'),
    path('jobs_test/', views.jobs_test, name='fl_jobs_test'),
    path("load_job_details/", views.load_job_details, name="load_job_details"),
     path("submit-quote/", views.submit_quote, name="submit_quote"),
    path('logout/', views.logout, name='logout'),
    # path('job_detail_partial', views.load_job_details, name='job_detail_partial'),
    path('projectTracking/', views.projectTracking, name='fl_projectTracking'),
    path('singleProjectTracking/', views.singleProjectTracking, name='fl_singleProjectTracking'),
    path('submit_contact/', views.fl_contact, name='fl_contact'),
  
]