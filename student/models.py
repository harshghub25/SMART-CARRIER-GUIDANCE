from django.db import models
from django.contrib.auth.models import User

class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    interest = models.CharField(max_length=100)
    graduation_year = models.IntegerField()
    profile_completed = models.BooleanField(default=False)

    def __str__(self):
        return self.name
