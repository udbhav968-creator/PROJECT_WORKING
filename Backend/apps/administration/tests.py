from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class SystemHealthTests(APITestCase):
    def test_health_check_returns_200(self):
        response = self.client.get(reverse("system-health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "healthy")
        self.assertTrue(response.data["database_connected"])

    def test_health_response_has_timestamp(self):
        response = self.client.get(reverse("system-health"))
        self.assertIn("timestamp", response.data)


class SeedDemoDataTests(APITestCase):
    def test_seed_creates_records(self):
        response = self.client.post(reverse("seed-demo-data"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["success"])

    def test_seed_idempotent(self):
        self.client.post(reverse("seed-demo-data"))
        response = self.client.post(reverse("seed-demo-data"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("already exists", response.data["message"])


class AdminDashboardTests(APITestCase):
    def setUp(self):
        self.client.post(reverse("seed-demo-data"))

    def test_dashboard_returns_correct_structure(self):
        response = self.client.get(reverse("admin-dashboard"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("stats", response.data)
        self.assertIn("recent_logs", response.data)

    def test_dashboard_stats_have_required_keys(self):
        response = self.client.get(reverse("admin-dashboard"))
        stats = response.data["stats"]
        for key in [
            "total_users", "active_users", "total_appointments",
            "scheduled_appointments", "completed_appointments",
            "cancelled_appointments", "total_audit_logs",
        ]:
            self.assertIn(key, stats)

    def test_dashboard_user_count_correct(self):
        response = self.client.get(reverse("admin-dashboard"))
        self.assertGreaterEqual(response.data["stats"]["total_users"], 1)

    def test_dashboard_appointment_count_correct(self):
        response = self.client.get(reverse("admin-dashboard"))
        self.assertGreaterEqual(response.data["stats"]["total_appointments"], 2)


class AuditLogListTests(APITestCase):
    def setUp(self):
        self.client.post(reverse("seed-demo-data"))
        self.client.get(reverse("admin-dashboard"))

    def test_audit_log_list_returns_200(self):
        response = self.client.get(reverse("audit-log-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audit_log_list_is_paginated(self):
        response = self.client.get(reverse("audit-log-list"))
        self.assertIn("count", response.data)
        self.assertIn("results", response.data)
