from django.urls import path
from . import views

urlpatterns = [
    path('', views.cl_index, name='cl_index'),
    path('postajob/', views.cl_postajob, name='cl_postajob'),
    path('aboutus/', views.cl_aboutus, name='cl_aboutus'),
    path('industries/', views.cl_industries, name='cl_industries'),
    path('profile/', views.cl_profile, name='cl_profile'),
    path('test/', views.cl_test, name='cl_test'),
    path('logout/', views.cl_logout, name='cl_logout'),
    path('edit_profile/', views.edit_profile, name='cl_edit_profile'),
    path('submit_contact/', views.cl_contact, name='cl_contact'),
    path('ongoingProjects/', views.cl_ongoingProjects, name='cl_ongoingProjects'),
    path('singleOngoingProject/', views.cl_singleOgProject, name='cl_singleOgProject'),
    path('singleViewBid/', views.cl_singleViewBid, name='cl_singleViewBid'),
    path('viewBids/', views.cl_viewBids, name='cl_viewBids'),
    path('bidApproved/', views.cl_bidApproved, name='cl_bidApproved'),
    path('bidRejected/', views.cl_bidRejected, name='cl_bidRejected'),
  
]