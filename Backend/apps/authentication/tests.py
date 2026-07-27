from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase
from apps.authentication.models import RoleModel, UserProfileModel


class AuthenticationModelTests(APITestCase):
    def setUp(self):
        self.role = RoleModel.objects.create(
            name="Doctor",
            description="Clinical Medical Doctor"
        )
        self.profile = UserProfileModel.objects.create(
            email="doctor@clinic.com",
            full_name="Dr. Jane Doe",
            role=self.role,
            is_active=True
        )

    def test_role_creation(self):
        self.assertEqual(self.role.name, "Doctor")
        self.assertEqual(str(self.role), "Doctor")

    def test_user_profile_creation(self):
        self.assertEqual(self.profile.email, "doctor@clinic.com")
        self.assertEqual(self.profile.role.name, "Doctor")
        self.assertEqual(str(self.profile), "doctor@clinic.com (Dr. Jane Doe)")


class JWTAuthenticationAPITests(APITestCase):
    def setUp(self):
        self.username = "clinic_admin"
        self.password = "SecurePassword123!"
        self.user = User.objects.create_user(
            username=self.username,
            password=self.password,
            email="admin@clinic.com"
        )

    def test_jwt_token_obtain_success(self):
        url = reverse("token_obtain_pair")
        payload = {
            "username": self.username,
            "password": self.password,
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("access", response.data)
        self.assertIn("refresh", response.data)

    def test_jwt_token_obtain_invalid_credentials(self):
        url = reverse("token_obtain_pair")
        payload = {
            "username": self.username,
            "password": "WrongPassword!",
        }
        response = self.client.post(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertFalse(response.data["success"])

    def test_jwt_token_refresh_success(self):
        obtain_url = reverse("token_obtain_pair")
        obtain_payload = {
            "username": self.username,
            "password": self.password,
        }
        obtain_response = self.client.post(obtain_url, obtain_payload, format="json")
        refresh_token = obtain_response.data["refresh"]

        refresh_url = reverse("token_refresh")
        refresh_payload = {"refresh": refresh_token}
        refresh_response = self.client.post(refresh_url, refresh_payload, format="json")
        self.assertEqual(refresh_response.status_code, status.HTTP_200_OK)
        self.assertIn("access", refresh_response.data)
