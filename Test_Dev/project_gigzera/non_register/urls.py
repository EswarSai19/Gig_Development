
from django.urls import path
from . import views

app_name = 'non_register'

urlpatterns = [
    path('', views.index, name='index'),
    path('test/', views.test, name='test'),
    path('jobs/', views.jobs, name='jobs'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('industries/', views.industries, name='industries'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('forget/', views.forget, name='forget'),
    path('postajob/', views.postajob, name='postajob'),
    path('findajob/', views.findajob, name='findajob'),
]