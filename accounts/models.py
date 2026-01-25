from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    full_name = models.CharField(max_length=100)
    education = models.CharField(max_length=100)
    field_stream = models.CharField(max_length=100)
    interests = models.CharField(max_length=100)
    skill_level = models.CharField(max_length=50)
    career_goal = models.TextField(blank=True)   # optional
    profile_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username
