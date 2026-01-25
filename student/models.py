from django.db import models
from django.conf import settings
# Create your models here.
 
class studentprofile(models.Model):
    user=models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='student_profile'
    )

    name=models.CharField(max_length=100)
    intrest=models.CharField(max_length=100)
    degree=models.CharField(max_length=100)
    graduation_year=models.IntegerField()

    def __str__(self):
        return self.user.username
    
class skill(models.Model):
    skills=models.CharField(max_length=100)
    category=models.CharField(max_length=100)

    def __str__(self):
        return self.skills
    
class studentskill(models.Model):
    student=models.ForeignKey(
        studentprofile,
        on_delete=models.CASCADE
    )
    Skill=models.ForeignKey(
        skill,
        on_delete=models.CASCADE

    )
    level=models.IntegerField()

    def __str__(self):
        return f"{self.student}-{self.Skill}"