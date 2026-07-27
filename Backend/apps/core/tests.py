import uuid
from django.test import TestCase
from rest_framework.test import APIRequestFactory
from rest_framework.exceptions import ValidationError, PermissionDenied
from apps.core.models import TimeStampedModel
from apps.core.exceptions import custom_exception_handler
from apps.administration.models import AppointmentModel


class CoreModelTests(TestCase):
    def test_timestamped_model_uuid_generation(self):
        appointment = AppointmentModel.objects.create(
            patient_name="Test Patient",
            patient_phone="+91 9990001112",
            doctor_name="Dr. Test",
            appointment_date="2026-08-01T10:00:00Z",
        )
        self.assertIsInstance(appointment.id, uuid.UUID)
        self.assertIsNotNone(appointment.created_at)
        self.assertIsNotNone(appointment.updated_at)
        self.assertFalse(appointment.is_deleted)

    def test_soft_delete_and_restore(self):
        appointment = AppointmentModel.objects.create(
            patient_name="Test Patient Soft Delete",
            patient_phone="+91 9990001113",
            doctor_name="Dr. Test",
            appointment_date="2026-08-01T10:00:00Z",
        )
        appointment_id = appointment.id

        # Soft delete
        appointment.delete()
        self.assertFalse(AppointmentModel.objects.filter(id=appointment_id).exists())
        self.assertTrue(AppointmentModel.all_objects.filter(id=appointment_id).exists())

        # Restore
        soft_deleted_obj = AppointmentModel.all_objects.get(id=appointment_id)
        soft_deleted_obj.restore()
        self.assertTrue(AppointmentModel.objects.filter(id=appointment_id).exists())


class CustomExceptionHandlerTests(TestCase):
    def test_custom_exception_handler_validation_error(self):
        exc = ValidationError({"email": ["This field is required."]})
        response = custom_exception_handler(exc, context={})
        self.assertIsNotNone(response)
        self.assertFalse(response.data["success"])
        self.assertIn("email: This field is required.", response.data["errors"])

    def test_custom_exception_handler_permission_denied(self):
        exc = PermissionDenied("You do not have permission.")
        response = custom_exception_handler(exc, context={})
        self.assertIsNotNone(response)
        self.assertFalse(response.data["success"])
        self.assertIn("You do not have permission.", response.data["errors"])
