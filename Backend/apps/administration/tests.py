from django.urls import reverse
from django.utils import timezone
from rest_framework import status
from rest_framework.test import APITestCase
from apps.administration.models import AppointmentModel, AdminAuditLogModel, DoctorRosterModel


class NextGenInnovationsTests(APITestCase):
    """
    Automated Unit Test Suite for Razorpay, Twilio WhatsApp, and Gemini AI Summarizer APIs
    """
    def test_razorpay_order_creation(self):
        url = reverse("create-razorpay-order")
        response = self.client.post(url, {"amount_inr": 600, "currency": "INR"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["success"])
        self.assertIn("order_id", response.data)
        self.assertEqual(response.data["razorpay_key_id"], "rzp_test_PURE_HEALTH_2026")

    def test_whatsapp_notification_dispatch(self):
        url = reverse("send-whatsapp-notification")
        response = self.client.post(url, {"phone": "+91 9811122233", "token_number": "PURE-OPD-101", "doctor_name": "Dr. Divit Shah"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["whatsapp_status"], "QUEUED_AND_DISPATCHED")

    def test_ai_prescription_summarizer(self):
        url = reverse("summarize-prescription")
        response = self.client.post(url, {"text": "Patient has elevated HbA1c glucose levels and BP hypertension."})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("ai_summary", response.data)

    def test_gemini_ai_chatbot(self):
        url = reverse("chat-gemini-ai")
        response = self.client.post(url, {"message": "Hello Gemini AI!"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["ai_engine"], "Google Gemini 1.5 Pro AI")

    def test_system_metrics(self):
        url = reverse("system-metrics")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("db_query_latency_ms", response.data)

    def test_hospital_stats(self):
        url = reverse("hospital-stats")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("total_opd_appointments", response.data)

    def test_patient_feedback(self):
        url = reverse("patient-feedback")
        response = self.client.post(url, {"patient_name": "Test Patient", "rating": 5, "comments": "Great service!"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["feedback"]["rating_stars"], "5/5 ⭐")

    def test_icu_occupancy_telemetry(self):
        url = reverse("icu-occupancy")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["icu_ventilator_beds_available"], 14)

    def test_pharmacy_blood_bank_telemetry(self):
        url = reverse("pharmacy-blood-bank")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["pharmacy_icu_drugs_status"], "FULL_STOCK")

    def test_unified_ai_model_suite(self):
        url = reverse("ai-model-suite")
        response = self.client.post(url, {"symptoms": "chest pain", "lab_text": "HbA1c 8.4%"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("paradigms", response.data)
        self.assertEqual(response.data["paradigms"]["1_supervised_learning"]["triage_category"], "EMERGENCY_RED_ALERT")

    def test_mlops_pipeline(self):
        url = reverse("mlops-pipeline")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["mlops_pipeline_status"], "HEALTHY_ACTIVE")
        self.assertIn("model_registry", response.data)

    def test_deep_train_models(self):
        url = reverse("deep-train-models")
        response = self.client.post(url, {"epochs": 50})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["status"], "COMPLETED_OPTIMAL")
        self.assertEqual(len(response.data["models_trained"]), 4)

    def test_ambulance_dispatch(self):
        url = reverse("ambulance-dispatch")
        response = self.client.post(url, {"address": "Sector 12", "phone": "+91 9811122233"})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["success"])
        self.assertIn("dispatch_details", response.data)
        self.assertEqual(response.data["dispatch_details"]["estimated_eta_minutes"], 4.5)

    def test_kaggle_github_datasets(self):
        url = reverse("kaggle-github-datasets")
        response = self.client.post(url, {"source": "KAGGLE_MIMIC_III"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["dataset_telemetry"]["records_ingested"], 150000)

    def test_train_kaggle_models(self):
        url = reverse("train-kaggle-models")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["status"], "DEEP_TRAINING_SUCCESSFUL")

    def test_next_gen_50_features(self):
        url = reverse("next-gen-50-features")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["total_next_gen_features"], 50)
        self.assertEqual(response.data["domain_categories"], 10)


class TokenTrackerTests(APITestCase):
    """
    Automated Unit Test Suite for TokenTrackerView API
    Author: Udbhav (udbhav968-creator <snojkumar968@gmail.com>)
    """
    def setUp(self):
        self.appointment = AppointmentModel.objects.create(
            patient_name="Tracking Test Patient",
            patient_phone="+91 9999888877",
            doctor_name="Dr. Divit Shah",
            department="General_Consultation",
            token_number="PURE-TRACK-101",
            appointment_date=timezone.now(),
            status="scheduled",
        )

    def test_token_tracking_success(self):
        url = reverse("appointment-track", kwargs={"token_number": "PURE-TRACK-101"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["token_number"], "PURE-TRACK-101")
        self.assertEqual(response.data["patient_name"], "Tracking Test Patient")

    def test_token_tracking_not_found(self):
        url = reverse("appointment-track", kwargs={"token_number": "INVALID-TOKEN-999"})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertFalse(response.data["success"])


class SystemHealthTests(APITestCase):
    def test_health_check_returns_200(self):
        response = self.client.get(reverse("system-health"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["status"], "healthy")
        self.assertTrue(response.data["database_connected"])
        self.assertIn("database_latency_ms", response.data)

    def test_health_response_has_meta(self):
        response = self.client.get(reverse("system-health"))
        self.assertIn("timestamp", response.data)
        self.assertIn("nabh_hipaa_compliance_status", response.data)


class SeedDemoDataTests(APITestCase):
    def test_seed_creates_records(self):
        response = self.client.post(reverse("seed-demo-data"))
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["success"])
        self.assertTrue(DoctorRosterModel.objects.exists())

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
        self.assertIn("doctor_roster_status", response.data)
        self.assertIn("department_breakdown", response.data)
        self.assertIn("recent_logs", response.data)

    def test_dashboard_stats_keys(self):
        response = self.client.get(reverse("admin-dashboard"))
        stats = response.data["stats"]
        for key in [
            "total_users", "active_users", "total_appointments",
            "scheduled_appointments", "in_consultation_appointments",
            "completed_appointments", "cancelled_appointments",
            "emergency_triage_count", "on_duty_doctors_count", "total_estimated_revenue_inr", "total_audit_logs",
        ]:
            self.assertIn(key, stats)


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
            doctor_name="Dr. Divit Shah",
            department="General_Consultation",
            priority="urgent",
            consultation_type="OPD",
            consultation_fee_inr=600.00,
            token_number="PURE-GEN-101",
            appointment_date=timezone.now(),
            status="scheduled",
            notes="Initial consultation",
        )

    def test_list_appointments(self):
        response = self.client.get(reverse("appointment-list-create"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["count"], 1)

    def test_create_appointment_auto_token_and_telehealth_link(self):
        payload = {
            "patient_name": "Suresh Raina",
            "patient_phone": "+91 8887776665",
            "patient_email": "suresh@example.com",
            "doctor_name": "Dr. Rahul Mehta",
            "department": "Cardiology",
            "priority": "emergency",
            "consultation_type": "Teleconsultation",
            "consultation_fee_inr": 1000.00,
            "appointment_date": timezone.now().isoformat(),
            "status": "scheduled",
            "notes": "Emergency telehealth consultation",
        }
        response = self.client.post(reverse("appointment-list-create"), payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn("PURE-OPD-", response.data["token_number"])
        self.assertIn("EMG-ALERT-", response.data["emergency_escalation_code"])
        self.assertIn("https://meet.jit.si/purehealth-opd-", response.data["video_room_url"])
        self.assertIn("PURE HEALTH CLINIC OPD CONFIRMATION", response.data["whatsapp_confirmation_text"])
        self.assertIn("recipient_phone", response.data["sms_notification_payload"])

    def test_printable_opd_slip_endpoint(self):
        url = reverse("appointment-pdf-slip", kwargs={"pk": self.appointment.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("PURE-GEN-101", response.data["printable_opd_slip_html"])

    def test_retrieve_appointment_detail(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["token_number"], "PURE-GEN-101")

    def test_update_appointment(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        payload = {
            "patient_name": "Rajesh Sharma",
            "patient_phone": "+91 9811122233",
            "patient_email": "rajesh@example.com",
            "doctor_name": "Dr. Divit Shah",
            "department": "General_Consultation",
            "priority": "urgent",
            "consultation_type": "OPD",
            "consultation_fee_inr": 600.00,
            "token_number": "PURE-GEN-101",
            "appointment_date": timezone.now().isoformat(),
            "status": "completed",
            "notes": "Consultation completed successfully",
        }
        response = self.client.put(url, payload, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.appointment.refresh_from_db()
        self.assertEqual(self.appointment.status, "completed")

    def test_soft_delete_appointment(self):
        url = reverse("appointment-detail", kwargs={"pk": self.appointment.id})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(AppointmentModel.objects.filter(id=self.appointment.id).exists())
        self.assertTrue(AppointmentModel.all_objects.filter(id=self.appointment.id).exists())
