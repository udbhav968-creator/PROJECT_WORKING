from django.db import models
from apps.core.models import TimeStampedModel


class AppointmentModel(TimeStampedModel):
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    ]

    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=50)
    patient_email = models.EmailField(blank=True, null=True)
    doctor_name = models.CharField(max_length=255)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='scheduled', db_index=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'appointments'

    def __str__(self):
        return f"Appointment: {self.patient_name} with {self.doctor_name} ({self.status})"


class AdminAuditLogModel(TimeStampedModel):
    admin_email = models.EmailField(db_index=True)
    action = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'admin_audit_logs'

    def __str__(self):
        return f"{self.admin_email} - {self.action} on {self.resource}"
