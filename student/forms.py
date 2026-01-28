from django import forms
from .models import StudentProfile

class OnboardingForm(forms.ModelForm):
    class Meta:
        model = StudentProfile
        fields = ['name', 'degree', 'interest', 'graduation_year']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'interest': forms.TextInput(attrs={'class': 'form-control'}),
            'graduation_year': forms.NumberInput(attrs={'class': 'form-control'}),
        }
