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
        self.assertIn("HEALTHY_ACTIVE", response.data["mlops_pipeline_status"])
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

    def test_genomic_sequencing(self):
        url = reverse("genomic-sequencing")
        response = self.client.post(url, {"gene": "BRCA1_PANEL"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("genomic_analysis", response.data)
        self.assertEqual(response.data["genomic_analysis"]["precision_oncology_score"], 98.6)

    def test_radiology_xray_ai(self):
        url = reverse("radiology-xray-ai")
        response = self.client.post(url, {"scan_type": "CHEST_XRAY_DICOM"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("radiology_ai_result", response.data)
        self.assertEqual(response.data["radiology_ai_result"]["confidence_score"], 0.978)

    def test_fine_tune_ai_models(self):
        url = reverse("fine-tune-ai-models")
        response = self.client.post(url, {"learning_rate": 0.0001})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["status"], "FINE_TUNING_COMPLETED_SUCCESS")
        self.assertEqual(len(response.data["tuned_model_metrics"]), 4)

    def test_send_email_notification(self):
        url = reverse("send-email-notification")
        response = self.client.post(url, {"email": "snojkumar968@gmail.com", "patient_name": "Udbhav"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["email_telemetry"]["recipient_email"], "snojkumar968@gmail.com")

    def test_live_queue_sse(self):
        url = reverse("live-queue-sse")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("current_live_event", response.data)
        self.assertEqual(response.data["current_live_event"]["active_token_calling"], "PURE-OPD-1001")

    def test_bulk_insert_clinical_data(self):
        url = reverse("bulk-insert-clinical-data")
        response = self.client.post(url, {"record_count": 50000})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertTrue(response.data["success"])
        self.assertIn("bulk_insertion_telemetry", response.data)
        self.assertEqual(response.data["bulk_insertion_telemetry"]["total_records_inserted"], 50000)

    def test_system_diagnostics(self):
        url = reverse("system-diagnostics")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["system_health_status"], "ALL_PIPELINES_100_PERCENT_HEALTHY")
        self.assertIn("diagnostics", response.data)

    def test_deep_ai_super_engine(self):
        url = reverse("deep-ai-super-engine")
        response = self.client.post(url, {"epochs": 100, "lora_rank": 16})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("super_engine_telemetry", response.data)
        self.assertEqual(len(response.data["super_engine_telemetry"]["trained_models"]), 6)

    def test_ai_suite_page(self):
        url = reverse("ai-suite-page")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn(b"UNIFIED ENTERPRISE AI SUPER-ENGINE FRAMEWORK", response.content)

    def test_security_audit(self):
        url = reverse("security-audit")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["security_tier"], "MILITARY_GRADE_ZERO_TRUST")
        self.assertIn("vulnerability_scan_results", response.data)

    def test_iot_medical_devices(self):
        url = reverse("iot-medical-devices")
        response = self.client.post(url, {"heart_rate": 80, "spo2_percentage": 98})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("iot_telemetry", response.data)
        self.assertEqual(response.data["iot_telemetry"]["vital_signs"]["heart_rate_bpm"], 80)

    def test_database_ai_ingestion(self):
        url = reverse("database-ai-ingestion")
        response = self.client.post(url, {"records_indexed": 500000})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("database_ai_telemetry", response.data)
        self.assertEqual(response.data["database_ai_telemetry"]["total_records_vectorized"], 500000)

    def test_voice_dictation(self):
        url = reverse("voice-dictation")
        response = self.client.post(url, {"audio_transcript": "Patient exhibits acute pharyngitis."})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("dictation_result", response.data)

    def test_cdss_agent(self):
        url = reverse("cdss-agent")
        response = self.client.post(url, {"symptoms": ["chest_pain"]})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("cdss_evaluation", response.data)

    def test_fhir_patient(self):
        url = reverse("fhir-patient")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data["resourceType"], "Patient")

    def test_cloudflare_security_server(self):
        url = reverse("cloudflare-security-server")
        response = self.client.post(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("cloudflare_security_binding", response.data)
        self.assertEqual(response.data["cloudflare_security_binding"]["proxy_status"], "PROXIED_ORANGE_CLOUD_ACTIVE")

    def test_pharmacy_order_tracking(self):
        url = reverse("pharmacy-order-tracking")
        response = self.client.post(url, {"rx_token": "RX-884920"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("pharmacy_fulfillment", response.data)

    def test_organ_transplant_matching(self):
        url = reverse("organ-transplant-matching")
        response = self.client.post(url, {"organ_type": "KIDNEY", "blood_type": "O_NEGATIVE"})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("transplant_match_result", response.data)

    def test_traffic_management_server(self):
        url = reverse("traffic-management-server")
        response = self.client.post(url, {"max_throughput_req_sec": 10000})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("traffic_management_telemetry", response.data)
        self.assertEqual(response.data["traffic_management_telemetry"]["edge_cache_hit_rate"], "99.4%")


class EndToEndIntegrationTestSuite(APITestCase):
    """
    **Deep End-to-End System & Cross-Module Integration Test Suite**
    Validates complete user journeys across Auth, AI Triage, IoT Telemetry, Emergency Ambulance, and Pharmacy Drones.
    """

    def test_e2e_patient_registration_login_flow(self):
        reg_url = reverse("auth-register")
        payload = {
            "username": "integration_patient",
            "email": "integration_patient@clinic.com",
            "password": "SecurePassword123!",
            "full_name": "Integration Patient",
            "role_name": "Patient"
        }
        res_reg = self.client.post(reg_url, payload, format="json")
        self.assertEqual(res_reg.status_code, status.HTTP_201_CREATED)
        self.assertTrue(res_reg.data["success"])

    def test_e2e_iot_critical_telemetry_ambulance_trigger(self):
        iot_url = reverse("iot-medical-devices")
        payload = {"heart_rate": 145, "spo2_percentage": 85}
        res = self.client.post(iot_url, payload, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["iot_telemetry"]["clinical_triage_status"], "CRITICAL_EMERGENCY_ALERT")

    def test_end_to_end_user_journey_emergency_and_drone_fulfillment(self):
        # 1. IoT Anomaly Triage
        iot_url = reverse("iot-medical-devices")
        iot_res = self.client.post(iot_url, {"heart_rate": 150, "spo2_percentage": 84})
        self.assertEqual(iot_res.status_code, status.HTTP_200_OK)

        # 2. Ambulance Dispatch
        amb_url = reverse("ambulance-dispatch")
        amb_res = self.client.post(amb_url, {"location": "Sector 62, Noida"})
        self.assertIn(amb_res.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])

        # 3. Medical Drone Fulfillment
        drone_url = reverse("pharmacy-order-tracking")
        drone_res = self.client.post(drone_url, {"rx_token": "RX-EMERGENCY-991"})
        self.assertEqual(drone_res.status_code, status.HTTP_200_OK)
        self.assertEqual(drone_res.data["pharmacy_fulfillment"]["delivery_mode"], "AUTONOMOUS_MEDICAL_DRONE")

    def test_e2e_ai_triage_and_super_engine_training(self):
        engine_url = reverse("deep-ai-super-engine")
        res = self.client.post(engine_url, {"epochs": 100}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertTrue(res.data["success"])
        self.assertIn("super_engine_telemetry", res.data)

    def test_e2e_pharmacy_drone_express_fulfillment(self):
        rx_url = reverse("pharmacy-order-tracking")
        res = self.client.post(rx_url, {"rx_token": "RX-INTEGRATION-999"}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["pharmacy_fulfillment"]["delivery_mode"], "AUTONOMOUS_MEDICAL_DRONE")

    def test_e2e_organ_transplant_hla_matching(self):
        match_url = reverse("organ-transplant-matching")
        res = self.client.post(match_url, {"organ_type": "HEART", "blood_type": "O_NEGATIVE"}, format="json")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn("hla_match_score", res.data["transplant_match_result"])





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


class MegaPipelineRealWorldDatasetTestSuite(APITestCase):
    """
    Real-World User & Dataset End-to-End Test Suite (MIMIC-III, NIH ChestX-ray14, UCI Heart)
    Validates dynamic, non-default inputs across full MLOps and clinical pipeline.
    """
    def test_mega_dataset_mlops_retraining(self):
        url = reverse("mega-dataset-mlops")
        response = self.client.post(url, {
            "dataset_name": "KAGGLE_MIMIC_III_AND_NIH_CHESTXRAY14",
            "epochs": 100,
            "target_f1_score": 0.998
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("mega_mlops_pipeline", response.data)
        self.assertEqual(len(response.data["mega_mlops_pipeline"]["ingested_corpora"]), 3)

    def test_real_world_patient_email_dispatch(self):
        url = reverse("send-email-notification")
        response = self.client.post(url, {
            "patient_email": "snojkumar968@gmail.com",
            "patient_name": "Udbhav",
            "token_number": "PURE-OPD-77112"
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["email_telemetry"]["recipient_email"], "snojkumar968@gmail.com")

    def test_real_world_genomic_sequencing_brca1(self):
        url = reverse("genomic-sequencing")
        response = self.client.post(url, {
            "dna_sequence": "ATGCGATCGATCGATCGATCGATCG",
            "target_genes": ["BRCA1", "EGFR", "TP53"]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("genomic_analysis", response.data)

    def test_real_world_cdss_knowledge_graph(self):
        url = reverse("cdss-agent")
        response = self.client.post(url, {
            "symptoms": ["acute_chest_pain", "diaphoresis", "shortness_of_breath"],
            "medications": ["Warfarin", "Aspirin"]
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertIn("cdss_evaluation", response.data)

    def test_real_world_traffic_server_high_concurrency(self):
        url = reverse("traffic-management-server")
        response = self.client.post(url, {
            "max_throughput_req_sec": 25000,
            "target_port": 8080
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue(response.data["success"])
        self.assertEqual(response.data["traffic_management_telemetry"]["max_throughput_capacity"], "25,000 req/sec")

