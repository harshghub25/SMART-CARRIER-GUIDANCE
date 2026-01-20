from django.urls import path
from  . import views
from .views import StudentOnboardingView

urlpatterns = [
    path('',views.home,name='home'),
    path('onboarding/', StudentOnboardingView.as_view()),
]