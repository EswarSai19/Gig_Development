from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('jobs/', views.jobs, name='jobs'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('industries/', views.industries, name='industries'),
    path('findajob/', views.findajob, name='findajob'),
    path('postajob/', views.postajob, name='postajob'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('forgot/', views.forgot, name='forgot'),
    path('submit_contact/', views.submit_contact, name='submit_contact'),
]
