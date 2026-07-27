from django.db import models
from apps.core.models import TimeStampedModel


class AppointmentModel(TimeStampedModel):
    """
    Pure Health Clinic Tier Clinical Appointment & OPD Token Model
    Inspired by Divit Pure Health Clinic (https://divitpurehealthclinic.com/)
    """
    STATUS_CHOICES = [
        ('scheduled', 'Scheduled'),
        ('in_consultation', 'In Consultation'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
        ('no_show', 'No Show'),
    ]

    DEPARTMENT_CHOICES = [
        ('General_Consultation', 'General Consultation & Preventive Care'),
        ('Diagnostic_Support', 'Diagnostic & Laboratory Support'),
        ('Chronic_Care', 'Chronic Disease Management (Diabetes/Hypertension)'),
        ('Wellness_Guidance', 'Wellness & Lifestyle Guidance'),
        ('Cardiology', 'Cardiology & Cardiovascular Care'),
        ('Neurology', 'Neurology & Nerve Health'),
        ('Orthopedics', 'Orthopedics & Joint Care'),
        ('Emergency_Care', 'Emergency & Urgent Triage'),
    ]

    PRIORITY_CHOICES = [
        ('routine', 'Routine OPD Consultation'),
        ('urgent', 'Urgent Referral'),
        ('emergency', 'Emergency Triage'),
    ]

    CONSULTATION_TYPE_CHOICES = [
        ('OPD', 'Outpatient Department (OPD)'),
        ('IPD', 'Inpatient Department (IPD)'),
        ('Emergency', 'Emergency Triage'),
        ('Teleconsultation', 'Tele-Health Consultation'),
    ]

    patient_name = models.CharField(max_length=255)
    patient_phone = models.CharField(max_length=50)
    patient_email = models.EmailField(blank=True, null=True)
    doctor_name = models.CharField(max_length=255)
    department = models.CharField(max_length=100, choices=DEPARTMENT_CHOICES, default='General_Consultation', db_index=True)
    priority = models.CharField(max_length=50, choices=PRIORITY_CHOICES, default='routine', db_index=True)
    consultation_type = models.CharField(max_length=50, choices=CONSULTATION_TYPE_CHOICES, default='OPD')
    token_number = models.CharField(max_length=100, blank=True, null=True, db_index=True)
    video_room_url = models.URLField(blank=True, null=True)
    appointment_date = models.DateTimeField()
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='scheduled', db_index=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        db_table = 'appointments'

    def __str__(self):
        return f"[{self.token_number or 'OPD'}] {self.patient_name} - {self.get_department_display()} ({self.status})"

    def generate_whatsapp_confirmation_message(self):
        return (
            f"🏥 *PURE HEALTH CLINIC OPD CONFIRMATION*\n"
            f"Patient: {self.patient_name}\n"
            f"Token No: *{self.token_number}*\n"
            f"Department: {self.get_department_display()}\n"
            f"Doctor: {self.doctor_name}\n"
            f"Date & Time: {self.appointment_date.strftime('%Y-%m-%d %H:%M')}\n"
            f"Status: {self.status.upper()}\n"
            f"Tele-Link: {self.video_room_url or 'N/A (In-Clinic OPD)'}"
        )


class DoctorRosterModel(TimeStampedModel):
    """
    Doctor Duty Roster & Shift Availability Tracker
    """
    DUTY_STATUS_CHOICES = [
        ('on_duty', 'On Duty (OPD Active)'),
        ('in_surgery', 'In Surgery / Procedure'),
        ('on_break', 'On Break'),
        ('off_duty', 'Off Duty'),
    ]

    doctor_name = models.CharField(max_length=255, unique=True)
    department = models.CharField(max_length=100, choices=AppointmentModel.DEPARTMENT_CHOICES, default='General_Consultation')
    shift_hours = models.CharField(max_length=100, default='09:00 AM - 05:00 PM')
    duty_status = models.CharField(max_length=50, choices=DUTY_STATUS_CHOICES, default='on_duty')
    room_number = models.CharField(max_length=50, default='OPD Room 101')

    class Meta:
        db_table = 'doctor_roster'

    def __str__(self):
        return f"{self.doctor_name} ({self.get_duty_status_display()}) - {self.room_number}"


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
