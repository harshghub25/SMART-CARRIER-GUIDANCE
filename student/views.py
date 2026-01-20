from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import studentprofile

class StudentOnboardingView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        studentprofile.objects.create(
            user=request.user,
            name=request.data.get('name'),
            degree=request.data.get('degree'),
            interest=request.data.get('interest'),
            graduation_year=request.data.get('graduation_year')
        )
        return Response({"message": "Profile created"})


# Create your views here.
def home(req):
    return render(req,'student/home.html')