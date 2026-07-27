from rest_framework import serializers
from apps.administration.models import AdminAuditLogModel, AppointmentModel, DoctorRosterModel


class AdminAuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdminAuditLogModel
        fields = ["id", "admin_email", "action", "resource", "severity", "compliance_category", "ip_address", "details", "created_at"]


class DoctorRosterSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorRosterModel
        fields = ["id", "doctor_name", "department", "consultation_fee_inr", "shift_hours", "duty_status", "room_number", "max_daily_patients", "current_queue_count", "updated_at"]


class AppointmentSerializer(serializers.ModelSerializer):
    whatsapp_confirmation_text = serializers.SerializerMethodField()
    sms_notification_payload = serializers.SerializerMethodField()

    class Meta:
        model = AppointmentModel
        fields = [
            "id", "patient_name", "patient_phone", "patient_email",
            "doctor_name", "department", "priority", "consultation_type",
            "consultation_fee_inr", "token_number", "video_room_url", "emergency_escalation_code",
            "appointment_date", "status", "notes",
            "whatsapp_confirmation_text", "sms_notification_payload",
            "created_at", "updated_at",
        ]

    def get_whatsapp_confirmation_text(self, obj):
        return obj.generate_whatsapp_confirmation_message()

    def get_sms_notification_payload(self, obj):
        return obj.generate_sms_notification_payload()


class DepartmentStatsSerializer(serializers.Serializer):
    department = serializers.CharField()
    count = serializers.IntegerField()


class SystemStatsSerializer(serializers.Serializer):
    total_users = serializers.IntegerField()
    active_users = serializers.IntegerField()
    total_appointments = serializers.IntegerField()
    scheduled_appointments = serializers.IntegerField()
    in_consultation_appointments = serializers.IntegerField()
    completed_appointments = serializers.IntegerField()
    cancelled_appointments = serializers.IntegerField()
    emergency_triage_count = serializers.IntegerField()
    on_duty_doctors_count = serializers.IntegerField()
    total_estimated_revenue_inr = serializers.DecimalField(max_digits=12, decimal_places=2)
    total_audit_logs = serializers.IntegerField()


class AdminDashboardResponseSerializer(serializers.Serializer):
    success = serializers.BooleanField(default=True)
    institute = serializers.CharField(default="Pure Health Clinic Core")
    stats = SystemStatsSerializer()
    doctor_roster_status = DoctorRosterSerializer(many=True)
    department_breakdown = DepartmentStatsSerializer(many=True)
    recent_logs = AdminAuditLogSerializer(many=True)
