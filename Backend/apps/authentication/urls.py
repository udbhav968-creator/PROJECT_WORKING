from django.urls import path
from apps.authentication.views import (
    UserRegistrationView,
    UserLoginView,
    UserProfileView,
    MfaVerificationView,
)

urlpatterns = [
    path('register/', UserRegistrationView.as_view(), name='auth-register'),
    path('login/', UserLoginView.as_view(), name='auth-login'),
    path('profile/', UserProfileView.as_view(), name='auth-profile'),
    path('mfa-verify/', MfaVerificationView.as_view(), name='auth-mfa-verify'),
]
