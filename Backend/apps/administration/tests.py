from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from apps.administration.models import AppointmentModel, AdminAuditLogModel


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


class AppointmentManagementTests(APITestCase):
    def setUp(self):
        self.appointment = AppointmentModel.objects.create(
            patient_name="Alice Smith",
            patient_phone="+91 9998887770",
            patient_email="alice@example.com",
            doctor_name="Dr. House",
            appointment_date=timezone.now(),
            status="scheduled",
            notes="Initial consultation",
        )

    def test_list_appointments(self):
        response = self.client.get(reverse("appointment-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_appointment(self):
        payload = {
            "patient_name": "Bob Marley",
            "patient_phone": "+91 8887776665",
            "patient_email": "bob@example.com",
            "doctor_name": "Dr. Watson",
            "appointment_date": timezone.now().isoformat(),
            "status": "scheduled",
            "notes": "Follow-up checkup",
        }
        response = self.client.post(reverse("appointment-list-create"), payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(AppointmentModel.objects.count(), 2)
        # Verify audit log was created
        self.assertTrue(AdminAuditLogModel.objects.filter(action="CREATE_APPOINTMENT").exists())

    def test_retrieve_appointment_detail(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["patient_name"], "Alice Smith")

    def test_update_appointment(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        payload = {
            "patient_name": "Alice Smith",
            "patient_phone": "+91 9998887770",
            "patient_email": "alice@example.com",
            "doctor_name": "Dr. House",
            "appointment_date": timezone.now().isoformat(),
            "status": "completed",
            "notes": "Consultation completed successfully",
        }
        response = self.client.put(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, "completed")
        self.assertTrue(AdminAuditLogModel.objects.filter(action="UPDATE_APPOINTMENT").exists())

    def test_soft_delete_appointment(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Should no longer be returned by default Manager (soft-deleted)
        self.assertFalse(AppointmentModel.objects.filter(id=self.appointment.id).exists())
        # Should still exist in database via all_objects
        self.assertTrue(AppointmentModel.all_objects.filter(id=self.appointment.id).exists())
        self.assertTrue(AdminAuditLogModel.objects.filter(action="DELETE_APPOINTMENT").exists())
