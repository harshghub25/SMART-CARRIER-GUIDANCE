from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import OnboardingForm
from .models import StudentProfile


@login_required
def onboarding(request):
    # sirf existing profile lao, create mat karo
    profile = StudentProfile.objects.filter(user=request.user).first()

    # agar profile complete hai → dashboard
    if profile and profile.profile_completed:
        return redirect('student:dashboard')

    if request.method == "POST":
        form = OnboardingForm(request.POST, instance=profile)

        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.profile_completed = True
            profile.save()
            return redirect('student:dashboard')
    else:
        form = OnboardingForm(instance=profile)

    return render(request, 'student/onboarding.html', {'form': form})


import pickle
import os
from student.functions import get_ai_career_suggestion


@login_required
def dashboard(request):
    profile = StudentProfile.objects.filter(user=request.user).first()
    print(profile)

    if not profile or not profile.profile_completed:
        return redirect('student:onboarding')

    career = get_ai_career_suggestion(profile)

    if not career:
        # Default career (fallback rule-based)
        career = "Explore skills → Internship → Specialization"


    return render(request, "student/dashboard.html", {
        "profile": profile,
        "career": career
    })
