from django import forms
from .models import StudentProfile

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['full_name', 'education', 'field_stream', 'interests', 'skill_level', 'career_goal']
        widgets = {
            'full_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your full name'}),
            'education': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('10th', '10th'),
                ('12th', '12th'),
                ('Diploma', 'Diploma'),
                ('Graduate', 'Graduate'),
                ('Post Graduate', 'Post Graduate')
            ]),
            'field_stream': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'e.g. Science, Commerce'}),
            'interests': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('Computer Technologies','Computer Technologies'),
                ('Sports','Sports'),
                ('Arts','Arts'),
                ('Design','Design'),
                ('Business / Management','Business / Management'),
                ('Government Jobs','Government Jobs'),
                ('Other','Other')
            ]),
            'skill_level': forms.Select(attrs={'class': 'form-select'}, choices=[
                ('Beginner','Beginner'),
                ('Intermediate','Intermediate'),
                ('Advanced','Advanced')
            ]),
            'career_goal': forms.Textarea(attrs={'class': 'form-control', 'rows':3, 'placeholder': 'Describe your career goal briefly'})
        }
