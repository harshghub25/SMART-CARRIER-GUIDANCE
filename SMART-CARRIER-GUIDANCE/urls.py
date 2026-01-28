# SMART-CARRIER-GUIDANCE/urls.py
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),

    # Home page default
    path('', lambda request: render(request, 'home.html'), name='home'),

    # Accounts app
    path('accounts/', include('accounts.urls', namespace='accounts')),

    # Student app
    path('student/', include('student.urls', namespace='student')),
]
