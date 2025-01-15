
from django.urls import path, include
from . import views

app_name = 'freelancer'

urlpatterns = [
    path('', views.freelancer_index, name='fl_index'),
]