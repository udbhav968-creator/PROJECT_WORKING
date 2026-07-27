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
        self.assertIn("database_latency_ms", response.data)

    def test_health_response_has_aiims_meta(self):
        response = self.client.get(reverse("system-health"))
        self.assertIn("timestamp", response.data)
        self.assertIn("nabh_hipaa_compliance_status", response.data)


class SeedDemoDataTests(APITestCase):
    def test_seed_creates_aiims_records(self):
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
        self.assertIn("department_breakdown", response.data)
        self.assertIn("recent_logs", response.data)

    def test_dashboard_stats_have_aiims_keys(self):
        response = self.client.get(reverse("admin-dashboard"))
        stats = response.data["stats"]
        for key in [
            "total_users", "active_users", "total_appointments",
            "scheduled_appointments", "in_consultation_appointments",
            "completed_appointments", "cancelled_appointments",
            "emergency_triage_count", "total_audit_logs",
        ]:
            self.assertIn(key, stats)

    def test_dashboard_department_breakdown(self):
        response = self.client.get(reverse("admin-dashboard"))
        breakdown = response.data["department_breakdown"]
        self.assertIsInstance(breakdown, list)
        self.assertGreaterEqual(len(breakdown), 1)


class AuditLogListTests(APITestCase):
    def setUp(self):
        self.client.post(reverse("seed-demo-data"))
        self.client.get(reverse("admin-dashboard"))

    def test_audit_log_list_returns_200(self):
        response = self.client.get(reverse("audit-log-list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_audit_log_severity_filter(self):
        response = self.client.get(reverse("audit-log-list") + "?severity=INFO")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("results", response.data)


class AppointmentManagementTests(APITestCase):
    def setUp(self):
        self.appointment = AppointmentModel.objects.create(
            patient_name="Rajesh Sharma",
            patient_phone="+91 9811122233",
            patient_email="rajesh@example.com",
            doctor_name="Dr. Balram Bhargava",
            department="Cardiology",
            priority="urgent",
            consultation_type="OPD",
            token_number="AIIMS-CARD-101",
            appointment_date=timezone.now(),
            status="scheduled",
            notes="Initial ECG examination",
        )

    def test_list_appointments(self):
        response = self.client.get(reverse("appointment-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_appointment_auto_token(self):
        payload = {
            "patient_name": "Suresh Raina",
            "patient_phone": "+91 8887776665",
            "patient_email": "suresh@example.com",
            "doctor_name": "Dr. Guleria",
            "department": "Emergency_Care",
            "priority": "emergency",
            "consultation_type": "Emergency",
            "appointment_date": timezone.now().isoformat(),
            "status": "scheduled",
            "notes": "Emergency triage evaluation",
        }
        response = self.client.post(reverse("appointment-list-create"), payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("AIIMS-OPD-", response.data["token_number"])
        self.assertEqual(AppointmentModel.objects.count(), 2)
        # Verify critical severity audit log was created
        self.assertTrue(AdminAuditLogModel.objects.filter(severity="CRITICAL").exists())

    def test_retrieve_appointment_detail(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["token_number"], "AIIMS-CARD-101")

    def test_update_appointment(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        payload = {
            "patient_name": "Rajesh Sharma",
            "patient_phone": "+91 9811122233",
            "patient_email": "rajesh@example.com",
            "doctor_name": "Dr. Balram Bhargava",
            "department": "Cardiology",
            "priority": "urgent",
            "consultation_type": "OPD",
            "token_number": "AIIMS-CARD-101",
            "appointment_date": timezone.now().isoformat(),
            "status": "completed",
            "notes": "ECG completed successfully",
        }
        response = self.client.put(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, "completed")
        self.assertTrue(AdminAuditLogModel.objects.filter(action="UPDATE_AIIMS_APPOINTMENT").exists())

    def test_soft_delete_appointment(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AppointmentModel.objects.filter(id=self.appointment.id).exists())
        self.assertTrue(AppointmentModel.all_objects.filter(id=self.appointment.id).exists())
        self.assertTrue(AdminAuditLogModel.objects.filter(action="DELETE_AIIMS_APPOINTMENT").exists())
