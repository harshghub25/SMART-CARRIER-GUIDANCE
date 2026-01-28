# student/urls.py
from django.urls import path
from . import views

app_name = "student"

urlpatterns = [
    path('onboarding/', views.onboarding, name='onboarding'),
    path('dashboard/', views.dashboard, name='dashboard'),
]
