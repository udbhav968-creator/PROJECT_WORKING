from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class AdminDashboardAPITests(APITestCase):
    def test_health_check_endpoint(self):
        url = reverse('system-health')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['status'], 'healthy')
        self.assertTrue(response.data['database_connected'])

    def test_seed_demo_data(self):
        url = reverse('seed-demo-data')
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data['success'])

    def test_admin_dashboard_summary(self):
        # Seed first
        self.client.post(reverse('seed-demo-data'))

        url = reverse('admin-dashboard')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data['success'])
        self.assertGreaterEqual(response.data['stats']['total_users'], 1)
        self.assertGreaterEqual(response.data['stats']['total_appointments'], 2)
