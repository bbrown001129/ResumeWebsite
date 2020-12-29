from django.urls import path
from ResumeWebsite import views

urlpatterns = [
    path('', views.homeAction, name='home'),
]