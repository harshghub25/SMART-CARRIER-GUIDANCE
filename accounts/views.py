from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .models import StudentProfile
from .forms import StudentProfileForm


# ---------------- SIGNUP ----------------
def signup_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("signup")

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )

        login(request, user)
        return redirect("onboarding")   # ✅ ALWAYS onboarding after signup

    return render(request, "accounts/signup.html")


# ---------------- LOGIN ----------------
def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect("dashboard")
        else:
            messages.error(request, "Invalid credentials")
            return redirect("login")

    return render(request, "accounts/login.html")


# ---------------- LOGOUT ----------------
def logout_view(request):
    logout(request)
    return redirect("login")


# ---------------- ONBOARDING ----------------
@login_required
def onboarding(request):
    profile, created = StudentProfile.objects.get_or_create(user=request.user)

    if profile.profile_completed:
        return redirect("dashboard")

    if request.method == "POST":
        form = StudentProfileForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.profile_completed = True
            profile.save()
            return redirect("dashboard")   # ✅ THIS WORKS
    else:
        form = StudentProfileForm(instance=profile)

    return render(request, "accounts/onboarding.html", {"form": form})


# ---------------- DASHBOARD ----------------
@login_required
def dashboard(request):
    if not request.user.profile.profile_completed:
        return redirect("onboarding")

    return render(request, "accounts/dashboard.html")
