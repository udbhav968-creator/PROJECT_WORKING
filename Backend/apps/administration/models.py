from django.db import models
from apps.core.models import TimeStampedModel


class AppointmentModel(TimeStampedModel):
    """
    AIIMS Delhi Tier Clinical Appointment & OPD Token Model
    """
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_consultation', 'In Consultation'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]

    DEPARTMENT_CHOICES = [
        ('Cardiology', 'Cardiology (CTVS)'),
        ('Neurology', 'Neurology & Neurosurgery'),
        ('Orthopedics', 'Orthopedics & Trauma'),
        ('Pediatrics', 'Pediatrics & Neonatology'),
        ('General_Medicine', 'General Medicine'),
        ('Emergency_Care', 'Emergency & Trauma Care'),
        ('Oncology', 'Medical & Surgical Oncology'),
    ]

    PRIORITY_CHOICES = [
        ('routine', 'Routine OPD'),
        ('urgent', 'Urgent Referral'),
        ('emergency', 'Critical / Emergency Triage'),
    ]

    CONSULTATION_TYPE_CHOICES = [
        ('OPD', 'Outpatient Department (OPD)'),
        ('IPD', 'Inpatient Department (IPD)'),
        ('Emergency', 'Emergency Care Triage'),
        ('Teleconsultation', 'AIIMS Tele-Medicine'),
    ]

    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=50)
    patient_email = models.EmailField(blank=True, null=True)
    doctor_name = models.CharField(max_length=255)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, default='General_Medicine', db_index=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='routine', db_index=True)
    consultation_type = models.CharField(max_length=50, choices=CONSULTATION_TYPE_CHOICES, default='OPD')
    token_number = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='scheduled', db_index=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'appointments'

    def __str__(self):
        return f"[{self.token_number or 'OPD'}] {self.patient_name} - {self.department} ({self.status})"


class AdminAuditLogModel(TimeStampedModel):
    """
    NABH & HIPAA Compliant Healthcare Admin Audit Log Model
    """
    SEVERITY_CHOICES = [
        ('INFO', 'Information'),
        ('WARNING', 'Warning / Overrides'),
        ('CRITICAL', 'Critical Emergency Action'),
    ]

    admin_email = models.EmailField(db_index=True)
    action = models.CharField(max_length=100)
    resource = models.CharField(max_length=100)
    severity = models.CharField(max_length=20, choices=SEVERITY_CHOICES, default='INFO', db_index=True)
    compliance_category = models.CharField(max_length=100, default='NABH_HIPAA_AUDIT')
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    details = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'admin_audit_logs'

    def __str__(self):
        return f"[{self.severity}] {self.admin_email} - {self.action} on {self.resource}"
